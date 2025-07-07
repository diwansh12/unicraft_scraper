from duckduckgo_search import DDGS

def get_urls_from_query(query, max_results=10):
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=max_results)
            return [r['href'] for r in results if 'href' in r]
    except Exception as e:
        print(f"Search error: {e}")
        return []
