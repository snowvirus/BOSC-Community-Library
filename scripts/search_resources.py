import csv
import sys
import os

def search_resources(query, filename='resources/resource-database.csv'):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return

    results = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Search in title, category, and description
            if (query.lower() in row['title'].lower() or 
                query.lower() in row['category'].lower() or 
                query.lower() in row['description'].lower()):
                results.append(row)
    
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_resources.py <query>")
        sys.exit(1)
    
    query = sys.argv[1]
    print(f"Searching for: '{query}'...\n")
    results = search_resources(query)
    
    if results:
        print(f"Found {len(results)} matches:\n")
        for res in results:
            print(f"- [{res['id']}] {res['title']}")
            print(f"  Category: {res['category']}")
            print(f"  Access: {res['access']}")
            print(f"  Description: {res['description']}")
            print("-" * 30)
    else:
        print("No matches found.")
