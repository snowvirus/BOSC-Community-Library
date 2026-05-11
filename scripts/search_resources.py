import argparse
import csv
import os


DEFAULT_DATABASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "resources",
    "resource-database.csv",
)

SEARCH_FIELDS = (
    "id",
    "title",
    "category",
    "provider",
    "target_audience",
    "connectivity",
    "description",
    "status",
)


def normalize(value):
    return (value or "").strip().lower()


def row_matches(row, query, category):
    if category and normalize(row.get("category")) != normalize(category):
        return False

    if not query:
        return True

    terms = normalize(query).split()
    searchable_text = " ".join(normalize(row.get(field)) for field in SEARCH_FIELDS)
    return all(term in searchable_text for term in terms)


def load_resources(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} not found.")

    with open(filename, mode="r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def search_resources(query="", category="", filename=DEFAULT_DATABASE):
    rows = load_resources(filename)
    return [row for row in rows if row_matches(row, query, category)]


def build_parser():
    parser = argparse.ArgumentParser(
        description="Search the BOSC Community Library resource database."
    )
    parser.add_argument(
        "query",
        nargs="?",
        default="",
        help="Keyword or phrase to search across resource fields.",
    )
    parser.add_argument(
        "-c",
        "--category",
        default="",
        help="Limit results to an exact category name, such as 'Digital Literacy'.",
    )
    parser.add_argument(
        "-f",
        "--file",
        default=DEFAULT_DATABASE,
        help="Path to the resource database CSV file.",
    )
    return parser


def print_result(resource):
    print(f"- [{resource['id']}] {resource['title']}")
    print(f"  Category: {resource['category']}")
    print(f"  Audience: {resource['target_audience']}")
    print(f"  Access: {resource['access']}")
    print(f"  Connectivity: {resource['connectivity']}")
    print(f"  License: {resource['license']}")
    print(f"  Status: {resource['status']}")
    print(f"  Description: {resource['description']}")
    print("-" * 30)


if __name__ == "__main__":
    args = build_parser().parse_args()

    search_label = args.query or "all resources"
    if args.category:
        search_label = f"{search_label} in category '{args.category}'"

    print(f"Searching for: {search_label}\n")

    try:
        results = search_resources(args.query, args.category, args.file)
    except FileNotFoundError as error:
        print(f"Error: {error}")
        raise SystemExit(1)

    if not results:
        print("No matches found.")
        raise SystemExit(0)

    print(f"Found {len(results)} matches:\n")
    for result in results:
        print_result(result)
