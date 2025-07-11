from typing import List, Optional
from pydantic import BaseModel

class Paper(BaseModel):
    pubmed_id: str
    title: str
    publication_date: str
    non_academic_authors: List[str]
    company_affiliations: List[str]
    corresponding_author_email: Optional[str]
