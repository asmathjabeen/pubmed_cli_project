import requests
import xml.etree.ElementTree as ET
import argparse
import csv

# Function to search PubMed by keyword
def search_pubmed(query):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 5
    }
    response = requests.get(url, params=params)
    data = response.json()
    ids = data['esearchresult']['idlist']
    return ids

# Function to fetch paper details by IDs
def fetch_details(ids):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    return response.text

# Function to parse XML, print results, and save to CSV
def parse_print_save(xml_data, query):
    root = ET.fromstring(xml_data)
    articles = root.findall(".//PubmedArticle")

    results = []

    for article in articles:
        title = article.find(".//ArticleTitle")
        abstract = article.find(".//AbstractText")
        authors = article.findall(".//Author")

        title_text = title.text if title is not None else "N/A"
        abstract_text = abstract.text if abstract is not None else "N/A"

        author_names = []
        if authors:
            for author in authors:
                last = author.find("LastName")
                first = author.find("ForeName")
                if last is not None and first is not None:
                    author_names.append(f"{first.text} {last.text}")

        authors_text = ", ".join(author_names) if author_names else "N/A"

        print("\n--- Paper ---")
        print("Title:", title_text)
        print("Abstract:", abstract_text)
        print("Authors:", authors_text)

        results.append({
            "Title": title_text,
            "Abstract": abstract_text,
            "Authors": authors_text
        })

    # Save to CSV
    csv_filename = f"{query.replace(' ', '_')}_papers.csv"
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Abstract", "Authors"])
        writer.writeheader()
        writer.writerows(results)
    print(f"\nResults saved to {csv_filename}")

# Main CLI function
def main():
    parser = argparse.ArgumentParser(description="Search PubMed papers by keyword.")
    parser.add_argument("query", help="Search query")
    args = parser.parse_args()

    ids = search_pubmed(args.query)
    if not ids:
        print("No results found.")
    else:
        xml_data = fetch_details(ids)
        parse_print_save(xml_data, args.query)

if __name__ == "__main__":
    main()
