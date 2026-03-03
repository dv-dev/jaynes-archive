(function () {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    let index;

    function initFlexSearch() {
        fetch(new URL('index.json', document.baseURI).toString())
            .then(response => response.json())
            .then(data => {
                index = new FlexSearch.Document({
                    document: {
                        id: 'permalink',
                        index: [
                            { field: 'title', tokenize: 'strict' },
                            { field: 'content', tokenize: 'strict' }
                        ],
                        store: ['title', 'permalink', 'year', 'content']
                    }
                });
                data.forEach(item => {
                    index.add(item);
                });
            });
    }

    function highlight(text, query) {
        if (!query) return text;
        
        const escapedQuery = query.trim().replace(/[.*+?^${}()|[\\]/g, '\\$&').replace(/\s+/g, '\\s+');
        const phraseRegex = new RegExp(`(\\b${escapedQuery}\\b)`, 'gi');
        
        // If the full phrase matches at word boundaries
        if (phraseRegex.test(text)) {
            return text.replace(phraseRegex, '<mark class="bg-blue-100 text-blue-900 rounded-sm px-0.5 font-medium">$1</mark>');
        }

        // Fallback: match individual terms but only at word boundaries
        const terms = query.trim().split(/\s+/).filter(t => t.length > 0);
        terms.sort((a, b) => b.length - a.length);
        
        let highlighted = text;
        terms.forEach(term => {
            const escapedTerm = term.replace(/[.*+?^${}()|[\\]/g, '\\$&');
            const re = new RegExp(`(\\b${escapedTerm}\\b)`, 'gi');
            highlighted = highlighted.replace(re, '<mark class="bg-blue-100 text-blue-900 rounded-sm px-0.5 font-medium">$1</mark>');
        });
        return highlighted;
    }

    function createSnippet(content, query) {
        if (!content || !query) return '';
        
        const escapedQuery = query.trim().replace(/[.*+?^${}()|[\\]/g, '\\$&').replace(/\s+/g, '\\s+');
        const phraseRegex = new RegExp(`\\b${escapedQuery}\\b`, 'i');
        const match = content.match(phraseRegex);
        
        let bestIndex = -1;
        if (match) {
            bestIndex = match.index;
        } else {
            // Fallback to first term at word boundary
            const terms = query.trim().split(/\s+/).filter(t => t.length > 0);
            for (const term of terms) {
                const escapedTerm = term.replace(/[.*+?^${}()|[\\]/g, '\\$&');
                const re = new RegExp(`\\b${escapedTerm}\\b`, 'i');
                const termMatch = content.match(re);
                if (termMatch) {
                    bestIndex = termMatch.index;
                    break;
                }
            }
        }

        if (bestIndex === -1) return content.slice(0, 200) + '...';

        const start = Math.max(0, bestIndex - 80);
        const end = Math.min(content.length, bestIndex + 120);
        let snippet = content.slice(start, end);

        if (start > 0) snippet = '...' + snippet;
        if (end < content.length) snippet = snippet + '...';

        return highlight(snippet, query);
    }

    function showResults() {
        const query = searchInput.value.trim();
        
        if (query === '') {
            searchResults.classList.add('hidden');
            return;
        }

        if (!index) return;

        const results = index.search(query, { enrich: true });
        searchResults.innerHTML = '';

        const seen = new Set();
        let uniqueResults = [];

        results.forEach(fieldResult => {
            fieldResult.result.forEach(result => {
                if (!seen.has(result.id)) {
                    seen.add(result.id);
                    uniqueResults.push(result);
                }
            });
        });

        // Strict Phrase Matching Filter
        const terms = query.toLowerCase().split(/\s+/).filter(t => t.length > 0);
        if (terms.length > 1) {
            uniqueResults = uniqueResults.filter(result => {
                const title = (result.doc.title || '').toLowerCase();
                const content = (result.doc.content || '').toLowerCase();
                const escapedQuery = query.replace(/[.*+?^${}()|[\\]/g, '\\$&').replace(/\s+/g, '\\s+');
                const phraseRegex = new RegExp(`\\b${escapedQuery}\\b`, 'i');
                return phraseRegex.test(title) || phraseRegex.test(content);
            });
        }

        uniqueResults.sort((a, b) => {
            const yearA = parseInt(a.doc.year) || 0;
            const yearB = parseInt(b.doc.year) || 0;
            return yearB - yearA;
        });

        if (uniqueResults.length > 0) {
            uniqueResults.forEach(result => {
                const item = document.createElement('a');
                item.href = result.doc.permalink;
                item.className = 'block p-4 border-b border-gray-100 hover:bg-gray-50 transition-colors last:border-0';
                
                const snippet = createSnippet(result.doc.content, query);
                
                item.innerHTML = `
                    <div class="flex justify-between items-start mb-1">
                        <div class="font-semibold text-blue-700">${highlight(result.doc.title, query)}</div>
                        <div class="text-[10px] font-bold text-gray-400 bg-gray-50 border border-gray-200 px-1.5 py-0.5 rounded ml-2 uppercase tracking-wider">${result.doc.year}</div>
                    </div>
                    <div class="text-xs text-gray-600 line-clamp-2 leading-relaxed">
                        ${snippet}
                    </div>
                `;
                searchResults.appendChild(item);
            });
            searchResults.classList.remove('hidden');
        } else {
            const noResults = document.createElement('div');
            noResults.className = 'p-4 text-gray-400 text-sm italic';
            noResults.textContent = `No results for "${query}"`;
            searchResults.appendChild(noResults);
            searchResults.classList.remove('hidden');
        }
    }

    if (searchInput) {
        initFlexSearch();
        searchInput.addEventListener('input', showResults);

        document.addEventListener('click', (e) => {
            if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
                searchResults.classList.add('hidden');
            }
        });
    }
})();
