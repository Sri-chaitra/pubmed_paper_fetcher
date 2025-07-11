from typing import List, Optional
from .models import Paper
from .filters import is_non_academic, extract_company
from Bio import Entrez

# IMPORTANT: Replace this with your actual email
Entrez.email = "chaitrapaladugula@gmail.com"

def fetch_pubmed_ids(query: str, debug: bool=False) -> List[str]:
    handle = Entrez.esearch(db="pubmed", term=query, retmax=50)
    record = Entrez.read(handle)
    ids = record["IdList"]
    if debug:
        print(f"[DEBUG] Found PubMed IDs: {ids}")
    return ids

def fetch_paper_metadata(pubmed_id: str, debug: bool=False) -> Optional[Paper]:
    handle = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
    records = Entrez.read(handle)
    try:
        article = records["PubmedArticle"][0]
        title = article["MedlineCitation"]["Article"]["ArticleTitle"]
        date_info = article["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["PubDate"]
        date_str = date_info.get("Year", "Unknown")

        authors = article["MedlineCitation"]["Article"].get("AuthorList", [])
        non_academic_authors = []
        company_affiliations = []
        corresponding_email = None

        for author in authors:
            affils = author.get("AffiliationInfo", [])
            for affil_info in affils:
                affil = affil_info.get("Affiliation", "")
                if is_non_academic(affil):
                    non_academic_authors.append(author.get("LastName", "Unknown"))
                    company_affiliations.append(extract_company(affil))
            if "ElectronicAddress" in author:
                corresponding_email = author["ElectronicAddress"]

        if not non_academic_authors:
            return None

        return Paper(
            pubmed_id=pubmed_id,
            title=title,
            publication_date=date_str,
            non_academic_authors=non_academic_authors,
            company_affiliations=company_affiliations,
            corresponding_author_email=corresponding_email
        )

    except Exception as e:
        if debug:
            print(f"[DEBUG] Error parsing PubMed ID {pubmed_id}: {e}")
        return None
