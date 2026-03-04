#!/usr/bin/env python3
"""Sequential QA runner for paper markdown files using codex exec.

This script:
- walks content/papers/*.md in deterministic order
- calls codex exec once per file
- stores resumable state in JSON
- shows a simple progress bar
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List


DEFAULT_STATE_FILE = "data/paper_qa_status.json"
DEFAULT_CONTENT_DIR = "content/papers"
DEFAULT_LOG_DIR = ".run_logs/paper_qa_logs"


@dataclass
class FileStatus:
    status: str
    attempts: int
    last_run_utc: str | None
    return_code: int | None
    error: str | None

    def as_dict(self) -> Dict[str, object]:
        return {
            "status": self.status,
            "attempts": self.attempts,
            "last_run_utc": self.last_run_utc,
            "return_code": self.return_code,
            "error": self.error,
        }


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_state(state_path: Path) -> Dict[str, object]:
    if not state_path.exists():
        return {}
    try:
        return json.loads(state_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_state(state_path: Path, state: Dict[str, object]) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_prompt(file_relpath: str) -> str:
    return f"""Perform QA and directly edit only this one markdown file: `{file_relpath}`.

Hard constraints (must follow exactly):
1. Do NOT change any paper content/meaning.
2. Do NOT change mathematical expressions, symbols, operators, variable names, or equation content.
3. You MAY add or adjust equation-numbering markup only (for example, display-equation tags/labels) when needed to match in-text Eq. references.
4. Ignore missing figures.

Allowed/required QA scope:
- Fix markdown structure/readability only:
  - split paragraphs properly to avoid giant text walls
  - enforce this rule: paragraph boundaries MUST be a blank line (double newline)
  - when one paragraph clearly ends and the next begins, convert `...sentence\nNext sentence...` to `...sentence\n\nNext sentence...`
  - do not keep prose paragraphs joined by a single newline where a visual paragraph break is intended
  - repair odd markdown table formatting
  - ensure markdown renders cleanly in Hugo+KaTeX
- Equation references:
  - if prose references equations like Eq. (7), Eqs. (2) and (3), etc., ensure the corresponding display equations show visible numbers
  - every referenced equation number should be discoverable in the document on a display equation
  - keep numbering consistent with existing references; do not invent new references in prose
  - prefer minimal numbering edits (tags/labels only), never expression edits
- Ensure abstract is not duplicated:
  - abstract should exist in metadata/front matter only
  - remove duplicate abstract text from body if present
- Normalize citations:
  - use proper footnote citation formatting
  - remove double-citation patterns like '(Smith 2018)' when duplicated with footnotes
- Remove extraneous metadata like 'Lecture given at ...' if it is not part of the paper body.

Output requirements:
- Apply edits directly to the file if needed.
- Keep edits minimal and structural.
- Before finishing, self-check:
  - all intended paragraph breaks are blank-line separated
  - no unresolved in-text Eq. references to missing display-equation numbers
- At the end, print a concise summary of what changed (or 'no changes').
"""


def build_remediation_prompt(file_relpath: str, issues: List[str]) -> str:
    issue_lines = "\n".join(f"- {issue}" for issue in issues)
    return f"""Run a focused second-pass QA on `{file_relpath}`.

Previously detected issues:
{issue_lines}

Hard constraints:
1. Do NOT change paper meaning/content.
2. Do NOT change math expression content (symbols/operators/variables).
3. You may add equation-numbering markup only when needed to satisfy in-text equation references.
4. Ignore missing figures.

Fix only the listed issues, minimally.
Paragraph rule: true paragraph boundaries must be a blank line (double newline).
Equation rule: if Eq. (n) is referenced in prose, ensure a visible display-equation number for n exists.
At end, print: 'remediation complete' with a short summary.
"""


def list_paper_files(content_dir: Path) -> List[Path]:
    return sorted(content_dir.glob("*.md"), key=lambda p: p.name.lower())


def print_progress(done: int, total: int, current: str, width: int = 34) -> None:
    ratio = 1.0 if total == 0 else done / total
    filled = int(ratio * width)
    bar = "#" * filled + "-" * (width - filled)
    msg = f"[{bar}] {done}/{total} | {current}"
    print("\r" + msg[:200], end="", flush=True)


def ensure_file_entries(state: Dict[str, object], files: List[str]) -> None:
    file_map = state.setdefault("files", {})
    if not isinstance(file_map, dict):
        state["files"] = {}
        file_map = state["files"]

    for relpath in files:
        if relpath not in file_map:
            file_map[relpath] = FileStatus(
                status="pending",
                attempts=0,
                last_run_utc=None,
                return_code=None,
                error=None,
            ).as_dict()
        elif isinstance(file_map[relpath], dict) and file_map[relpath].get("status") == "running":
            # Recover cleanly after interrupted runs.
            file_map[relpath]["status"] = "pending"

    # Mark files no longer present as skipped_missing_from_repo.
    for relpath in list(file_map.keys()):
        if relpath not in files and isinstance(file_map[relpath], dict):
            file_map[relpath]["status"] = "skipped_missing_from_repo"


def count_statuses(state: Dict[str, object]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    files = state.get("files", {})
    if not isinstance(files, dict):
        return counts
    for entry in files.values():
        if not isinstance(entry, dict):
            continue
        st = str(entry.get("status", "unknown"))
        counts[st] = counts.get(st, 0) + 1
    return counts


def run_file(repo_root: Path, relpath: str) -> subprocess.CompletedProcess[str]:
    prompt = build_prompt(relpath)
    cmd = [
        "codex",
        "exec",
        "--sandbox",
        "workspace-write",
        "--model",
        "gpt-5.3-codex",
        "-",
    ]
    return subprocess.run(
        cmd,
        cwd=str(repo_root),
        input=prompt,
        text=True,
        capture_output=True,
        check=False,
    )


def run_with_prompt(repo_root: Path, prompt: str) -> subprocess.CompletedProcess[str]:
    cmd = [
        "codex",
        "exec",
        "--sandbox",
        "workspace-write",
        "--model",
        "gpt-5.3-codex",
        "-",
    ]
    return subprocess.run(
        cmd,
        cwd=str(repo_root),
        input=prompt,
        text=True,
        capture_output=True,
        check=False,
    )


def extract_body(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    parts = text.split("\n---\n", 1)
    if len(parts) == 2:
        return parts[1]
    return text


def is_markdown_control_line(line: str) -> bool:
    s = line.strip()
    if not s:
        return True
    if s.startswith(("#", ">", "-", "*", "+", "|", "```", "~~~", ":::")):
        return True
    if re.match(r"^\d+\.\s+", s):
        return True
    if s.startswith("[^") and "]: " in s:
        return True
    return False


def find_suspicious_paragraph_breaks(text: str) -> List[int]:
    body = extract_body(text)
    lines = body.splitlines()
    suspicious: List[int] = []
    in_fence = False
    in_math_block = False
    for idx in range(1, len(lines)):
        prev_line = lines[idx - 1]
        curr_line = lines[idx]
        if prev_line.strip().startswith(("```", "~~~")):
            in_fence = not in_fence
        if "$$" in prev_line.strip():
            in_math_block = not in_math_block
        if in_fence or in_math_block:
            continue
        if not prev_line.strip() or not curr_line.strip():
            continue
        if is_markdown_control_line(prev_line) or is_markdown_control_line(curr_line):
            continue
        if len(prev_line.strip()) < 120 or len(curr_line.strip()) < 120:
            continue
        if not re.search(r'[.!?:"\')\]]\s*$', prev_line.strip()):
            continue
        if not re.match(r'^[A-Z"\'(\[]', curr_line.strip()):
            continue
        suspicious.append(idx + 1)
    return suspicious


def collect_eq_refs(text: str) -> List[int]:
    refs = re.findall(r"\bEqs?\.\s*\((\d+)\)", text)
    return sorted({int(n) for n in refs})


def collect_numbered_display_eqs(text: str) -> List[int]:
    nums = set()
    # KaTeX/Latex tags
    for n in re.findall(r"\\tag\{(\d+)\}", text):
        nums.add(int(n))
    # Common plain markers near display math in some papers
    for n in re.findall(r"(?m)^\s*\((\d+)\)\s*$", text):
        nums.add(int(n))
    return sorted(nums)


def validate_markdown(relpath: str, file_text: str) -> List[str]:
    issues: List[str] = []
    suspicious_breaks = find_suspicious_paragraph_breaks(file_text)
    if suspicious_breaks:
        issues.append(
            "Likely missing blank lines between paragraphs near body lines "
            + ", ".join(str(n) for n in suspicious_breaks[:8])
            + ("..." if len(suspicious_breaks) > 8 else "")
        )
    refs = collect_eq_refs(file_text)
    if refs:
        numbered = set(collect_numbered_display_eqs(file_text))
        missing = [n for n in refs if n not in numbered]
        if missing:
            issues.append(
                "In-text equation references exist but matching visible equation numbers were not found for "
                + ", ".join(str(n) for n in missing[:12])
                + ("..." if len(missing) > 12 else "")
            )
    return issues


def migrate_legacy_logs(repo_root: Path, log_dir: Path) -> None:
    legacy_dir = repo_root / "data" / "paper_qa_logs"
    if not legacy_dir.exists() or legacy_dir.resolve() == log_dir.resolve():
        return
    log_dir.mkdir(parents=True, exist_ok=True)
    for path in legacy_dir.glob("*.log"):
        target = log_dir / path.name
        if not target.exists():
            path.replace(target)
        else:
            path.unlink()
    try:
        legacy_dir.rmdir()
    except OSError:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(description="Run sequential markdown QA on content/papers via codex exec.")
    parser.add_argument("--repo-root", default=".", help="Repository root path (default: .)")
    parser.add_argument("--content-dir", default=DEFAULT_CONTENT_DIR, help=f"Relative content dir (default: {DEFAULT_CONTENT_DIR})")
    parser.add_argument("--state-file", default=DEFAULT_STATE_FILE, help=f"State JSON path (default: {DEFAULT_STATE_FILE})")
    parser.add_argument("--retry-failed", action="store_true", help="Retry files with status=failed")
    parser.add_argument("--force", action="store_true", help="Process all files regardless of prior status")
    parser.add_argument("--max-files", type=int, default=0, help="Optional cap on files processed this run (0 = no cap)")
    parser.add_argument("--log-dir", default=DEFAULT_LOG_DIR, help=f"Per-file log dir (default: {DEFAULT_LOG_DIR})")
    parser.add_argument(
        "--only",
        default="",
        help="Optional comma-separated list of specific markdown filenames or relative paths to process",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    content_dir = (repo_root / args.content_dir).resolve()
    state_path = (repo_root / args.state_file).resolve()
    log_dir = (repo_root / args.log_dir).resolve()
    migrate_legacy_logs(repo_root, log_dir)

    if not content_dir.exists():
        print(f"Error: content directory not found: {content_dir}", file=sys.stderr)
        return 1

    files_abs = list_paper_files(content_dir)
    files_rel = [str(p.relative_to(repo_root)) for p in files_abs]
    only_raw = [s.strip() for s in args.only.split(",") if s.strip()]
    only_set = set(only_raw)
    if only_set:
        files_rel = [
            rel
            for rel in files_rel
            if rel in only_set or Path(rel).name in only_set or Path(rel).stem in only_set
        ]
    total_files = len(files_rel)
    if total_files == 0:
        print(f"No markdown files found in {content_dir}")
        return 0

    state = load_state(state_path)
    state["schema_version"] = 1
    state["repo_root"] = str(repo_root)
    state["content_dir"] = str(Path(args.content_dir))
    state["state_file"] = str(Path(args.state_file))
    state["last_run_started_utc"] = utc_now()
    ensure_file_entries(state, files_rel)
    save_state(state_path, state)

    file_map = state["files"]
    assert isinstance(file_map, dict)

    to_process: List[str] = []
    for relpath in files_rel:
        entry = file_map.get(relpath, {})
        status = entry.get("status") if isinstance(entry, dict) else None
        if args.force:
            to_process.append(relpath)
            continue
        if status == "completed":
            continue
        if status == "failed" and not args.retry_failed:
            continue
        to_process.append(relpath)

    if args.max_files > 0:
        to_process = to_process[: args.max_files]

    planned = len(to_process)
    already_done = sum(
        1
        for relpath in files_rel
        if isinstance(file_map.get(relpath), dict) and file_map[relpath].get("status") == "completed"
    )

    print(f"Found {total_files} files. Already completed: {already_done}. Planned this run: {planned}.")
    if planned == 0:
        state["last_run_finished_utc"] = utc_now()
        state["counts"] = count_statuses(state)
        save_state(state_path, state)
        print("Nothing to process.")
        return 0

    processed_this_run = 0
    for relpath in to_process:
        processed_this_run += 1
        done_count = already_done + processed_this_run - 1
        print_progress(done_count, total_files, f"processing {Path(relpath).name}")

        entry = file_map.get(relpath, {})
        if not isinstance(entry, dict):
            entry = FileStatus("pending", 0, None, None, None).as_dict()
            file_map[relpath] = entry

        entry["status"] = "running"
        entry["attempts"] = int(entry.get("attempts", 0)) + 1
        entry["last_run_utc"] = utc_now()
        entry["return_code"] = None
        entry["error"] = None
        save_state(state_path, state)

        cp = run_file(repo_root, relpath)
        entry["return_code"] = cp.returncode
        entry["last_run_utc"] = utc_now()

        log_path = log_dir / f"{Path(relpath).stem}.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_text = (
            f"=== STDOUT ===\n{cp.stdout}\n\n"
            f"=== STDERR ===\n{cp.stderr}\n"
        )
        file_abs = repo_root / relpath
        validation_issues: List[str] = []
        remediation_cp: subprocess.CompletedProcess[str] | None = None

        if cp.returncode == 0 and file_abs.exists():
            file_text = file_abs.read_text(encoding="utf-8")
            validation_issues = validate_markdown(relpath, file_text)
            if validation_issues:
                remediation_prompt = build_remediation_prompt(relpath, validation_issues)
                remediation_cp = run_with_prompt(repo_root, remediation_prompt)
                if remediation_cp.returncode == 0 and file_abs.exists():
                    file_text = file_abs.read_text(encoding="utf-8")
                    validation_issues = validate_markdown(relpath, file_text)

        if remediation_cp is not None:
            log_text += (
                "\n=== REMEDIATION STDOUT ===\n"
                + (remediation_cp.stdout or "")
                + "\n\n=== REMEDIATION STDERR ===\n"
                + (remediation_cp.stderr or "")
                + "\n"
            )

        if validation_issues:
            log_text += "\n=== VALIDATION ISSUES ===\n" + "\n".join(validation_issues) + "\n"

        log_path.write_text(log_text, encoding="utf-8")

        if cp.returncode != 0:
            entry["status"] = "failed"
            stderr = (cp.stderr or "").strip()
            entry["error"] = stderr[-1000:] if stderr else "codex exec failed"
        elif remediation_cp is not None and remediation_cp.returncode != 0:
            entry["status"] = "failed"
            stderr = (remediation_cp.stderr or "").strip()
            entry["error"] = stderr[-1000:] if stderr else "remediation codex exec failed"
        elif validation_issues:
            entry["status"] = "failed"
            entry["error"] = "validation failed: " + "; ".join(validation_issues)[:900]
        else:
            entry["status"] = "completed"
            entry["error"] = None

        save_state(state_path, state)

    final_done = sum(
        1
        for relpath in files_rel
        if isinstance(file_map.get(relpath), dict) and file_map[relpath].get("status") == "completed"
    )
    print_progress(final_done, total_files, "done")
    print()

    state["last_run_finished_utc"] = utc_now()
    state["counts"] = count_statuses(state)
    save_state(state_path, state)

    completed_now = sum(
        1
        for relpath in to_process
        if isinstance(file_map.get(relpath), dict) and file_map[relpath].get("status") == "completed"
    )
    failed_now = planned - completed_now
    print(f"Run complete. Completed this run: {completed_now}. Failed this run: {failed_now}.")
    print(f"State: {state_path}")
    print(f"Logs:  {log_dir}")
    return 0 if failed_now == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
