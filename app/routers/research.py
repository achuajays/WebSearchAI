from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.services.agent_service import get_research_agent_service
from typing import Dict, Any, List

router = APIRouter(
    prefix="/api/research",
    tags=["research"],
    responses={404: {"description": "Not found"}},
)


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


@router.post("/run", response_model=Dict[str, Any])
async def run_research_agent(
        request: ResearchRequest,
        agent_service=Depends(get_research_agent_service)
):
    """
    Run the research agent to investigate the provided query.

    This endpoint processes a research query and returns findings from the research agent.

    Args:
        request (ResearchRequest): The request object containing the query
        agent_service: Research agent service injected via dependency

    Returns:
        Dict[str, Any]: Research results including findings and resource links

    Raises:
        HTTPException: 500 error if the research agent encounters any issues
    """
    try:
        result = agent_service.run_research(request.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running research agent: {str(e)}")