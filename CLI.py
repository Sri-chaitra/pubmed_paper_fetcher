import argparse
import csv
from papers_fetcher.fetcher import fetch_pubmed_ids, fetch_paper_metadata

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", type=str, help="PubMed query string")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file path")
    args = parser.parse_args()

    ids = fetch_pubmed_ids(args.query, debug=args.debug)
    papers = []
    for pid in ids:
        paper = fetch_paper_metadata(pid, debug=args.debug)
        if paper:
            papers.append(paper)

    if args.file:
        with open(args.file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                "PubmedID",
                "Title",
                "Publication Date",
                "Non-academic Author(s)",
                "Company Affiliation(s)",
                "Corresponding Author Email"
            ])
            for p in papers:
                writer.writerow([
                    p.pubmed_id,
                    p.title,
                    p.publication_date,
                    "; ".join(p.non_academic_authors),
                    "; ".join(p.company_affiliations),
                    p.corresponding_author_email or ""
                ])
        print(f"Results saved to {args.file}")
    else:
        for p in papers:
            print(p.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
