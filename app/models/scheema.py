from pydantic import BaseModel
from typing import List


class ResearchRequest(BaseModel):
    """
        Request model for research agent queries.

        Attributes:
            query (str): The research question or topic to investigate
        """
    query: str


class ResearchResponse(BaseModel):
    """
        Response model for research agent results.

        Attributes:
            research_data (str): The compiled research findings
            resource_links (List[str]): Links to sources used in the research
    """
    research_data: str
    resource_links: List[str]


class Format(BaseModel):
    """
        Response model for formatted text.

        Attributes:
            Summary (str): A summary of the text
            Reference (List[str]): A list of references used in the text
    """
    Summary: str
    Reference: List[str]


class FormatRequest(BaseModel):
    """
        Request model for formatting text.

        Attributes:
            prompt (str): The text to be formatted
    """
    prompt: str