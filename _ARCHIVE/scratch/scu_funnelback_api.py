from curl_cffi import requests
import json

# Explore Funnelback search.json API for comprehensive course extraction
# The search.json endpoint returns structured data including facets and results

params = {
    'collection': 'scu~sp-search',
    'profile': '_default',
    'f.Tabs|scu~ds-courses': 'Courses',
    'sort': 'title',
    'num_ranks': 100,
}

url = 'https://course-search.scu.edu.au/s/search.json'
r = requests.get(url, params=params, impersonate='chrome124', timeout=30)
data = r.json()

print('=== Funnelback Search API ===')
print(f'Response keys: {list(data.keys())}')

# Check the question/response structure
q = data.get('question', {})
print(f'\nQuery: {q.get("query")}')
print(f'Collection: {q.get("collection", {}).get("id")}')

# Look at response
resp = data.get('response', {})
print(f'\nResponse keys: {list(resp.keys())}')
print(f'Result count: {resp.get("resultCount")}')
print(f'Total matching: {resp.get("totalMatching")}')

# Check facets
facets = resp.get('facetCategories', [])
print(f'\nFacet categories: {len(facets)}')
for f in facets:
    print(f'  {f.get("name")}: {[c["data"] for c in f.get("categories", [])]}')

# Check result packet
packet = resp.get('resultPacket', {})
print(f'\nResults per page: {packet.get("resultsPerPage")}')
print(f'Current page/sort: {packet.get("currPage")}, {packet.get("currSort")}')

results = packet.get('results', [])
print(f'Results in this page: {len(results)}')

# Show sample results
if results:
    print('\n--- Sample Results (first 3) ---')
    for i, res in enumerate(results[:3]):
        print(f'\n  [{i+1}] Title: {res.get("title")}')
        print(f'       URL: {res.get("liveUrl")}')
        metas = res.get('metaData', {})
        for k, v in list(metas.items())[:5]:
            print(f'       {k}: {v}')

# Try getting more courses - search all
print('\n=== Try with no filters (all courses) ===')
params2 = {
    'collection': 'scu~sp-search',
    'profile': '_default',
    'query': '!padrenull',
    'sort': 'title',
    'num_ranks': 500,
}
r2 = requests.get(url, params=params2, impersonate='chrome124', timeout=30)
data2 = r2.json()
resp2 = data2.get('response', {})
print(f'Total matching: {resp2.get("totalMatching")}')
packet2 = resp2.get('resultPacket', {})
results2 = packet2.get('results', [])
print(f'Results returned: {len(results2)}')

# Check a few for metadata fields
if results2:
    print('\n--- Metadata keys from first result ---')
    print(list(results2[0].get('metaData', {}).keys()))
    print(f'\n--- First result meta ---')
    for k, v in results2[0].get('metaData', {}).items():
        if isinstance(v, str):
            print(f'  {k}: {v[:100]}')
        else:
            print(f'  {k}: {v}')
