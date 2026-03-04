#!/usr/bin/env python3
"""Build ZIP archives for currently available PDF sets."""

from __future__ import annotations

import zipfile
from pathlib import Path


def build_zip(src_dir: Path, out_zip: Path) -> int:
    src_dir.mkdir(parents=True, exist_ok=True)
    pdfs = sorted(src_dir.glob("*.pdf"), key=lambda p: p.name.lower())

    out_zip.parent.mkdir(parents=True, exist_ok=True)
    if out_zip.exists():
        out_zip.unlink()

    with zipfile.ZipFile(out_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for pdf in pdfs:
            zf.write(pdf, arcname=pdf.name)
    return len(pdfs)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    pdf_root = root / "static" / "pdfs"

    raw_count = build_zip(pdf_root / "raw", pdf_root / "raw.zip")
    clean_count = build_zip(pdf_root / "clean", pdf_root / "clean.zip")

    print(f"Built {pdf_root / 'raw.zip'} with {raw_count} files")
    print(f"Built {pdf_root / 'clean.zip'} with {clean_count} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
