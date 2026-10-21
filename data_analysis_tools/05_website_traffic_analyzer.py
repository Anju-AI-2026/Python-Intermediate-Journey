
# Website Traffic Analyzer
# Analyzes page visits, visitor counts, and traffic sources

from collections import Counter, defaultdict


def analyze_traffic(visits):
    page_views = Counter()
    source_views = Counter()
    visitors_by_page = defaultdict(set)
    unique_visitors = set()

    for visit in visits:
        page = visit["page"]
        visitor = visit["visitor_id"]
        source = visit["source"]

        page_views[page] += 1
        source_views[source] += 1
        visitors_by_page[page].add(visitor)
        unique_visitors.add(visitor)

    return page_views, source_views, visitors_by_page, unique_visitors


visits = [
    {"visitor_id": "V101", "page": "/home", "source": "Search"},
    {"visitor_id": "V102", "page": "/products", "source": "Social"},
    {"visitor_id": "V103", "page": "/home", "source": "Direct"},
    {"visitor_id": "V101", "page": "/products", "source": "Search"},
    {"visitor_id": "V104", "page": "/about", "source": "Direct"},
    {"visitor_id": "V105", "page": "/home", "source": "Social"},
    {"visitor_id": "V102", "page": "/contact", "source": "Social"},
    {"visitor_id": "V106", "page": "/products", "source": "Search"},
    {"visitor_id": "V103", "page": "/home", "source": "Direct"},
    {"visitor_id": "V107", "page": "/about", "source": "Search"},
    {"visitor_id": "V101", "page": "/contact", "source": "Direct"},
    {"visitor_id": "V108", "page": "/products", "source": "Social"},
]

page_views, source_views, visitors_by_page, unique_visitors = (
    analyze_traffic(visits)
)

print("=" * 65)
print("                  WEBSITE TRAFFIC ANALYZER")
print("=" * 65)

print("Total page views:", len(visits))
print("Unique visitors:", len(unique_visitors))
print("Pages visited:", len(page_views))

print("\nPAGE PERFORMANCE")
print("-" * 65)
print(f"{'Page':<20} {'Page Views':>12} {'Unique Visitors':>18}")
print("-" * 65)

for page, views in page_views.most_common():
    unique_page_visitors = len(visitors_by_page[page])
    print(f"{page:<20} {views:>12} {unique_page_visitors:>18}")

print("\nTRAFFIC SOURCES")
print("-" * 40)

for source, count in source_views.most_common():
    percentage = count / len(visits) * 100
    print(f"{source:<15} {count:>5} visits ({percentage:.1f}%)")

print("-" * 65)

if page_views:
    popular_page, views = page_views.most_common(1)[0]
    print(f"Most visited page: {popular_page} ({views} views)")

if source_views:
    top_source, count = source_views.most_common(1)[0]
    print(f"Top traffic source: {top_source} ({count} visits)")

print("=" * 65)
