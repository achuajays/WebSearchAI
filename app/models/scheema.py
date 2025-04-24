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
