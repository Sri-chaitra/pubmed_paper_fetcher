def is_non_academic(affiliation: str) -> bool:
    """
    Returns True if the affiliation looks non-academic.
    """
    lower = affiliation.lower()
    academic_keywords = [
        "university",
        "institute",
        "college",
        "hospital",
        "school",
        "center"
    ]
    return not any(word in lower for word in academic_keywords)

def extract_company(affiliation: str) -> str:
    """
    Extract the likely company name from the affiliation string.
    """
    return affiliation.split(",")[0].strip()
