from fastapi import APIRouter, Depends, HTTPException
from app.services.agent_service import get_research_agent_service
from app.models.scheema import ResearchRequest, ResearchResponse
from typing import Dict, Any

router = APIRouter(
    prefix="/api/research",
    tags=["research"],
    responses={404: {"description": "Not found"}},
)


@router.post("/run", response_model=ResearchResponse)
async def run_research_agent(
        request: ResearchRequest,
        agent_service=Depends(get_research_agent_service)
) -> ResearchResponse:
    """
    Run the research agent to investigate the provided query.

    This endpoint processes a research query and returns findings from the research agent.

    Args:
        request (ResearchRequest): The request object containing the query
        agent_service: Research agent service injected via dependency

    Returns:
        ResearchResponse: Research results including findings and resource links

    Raises:
        HTTPException: 500 error if the research agent encounters any issues
    """
    try:
        # Run the research agent with the provided query
        result: ResearchResponse = agent_service.run_research(request.query)
        return result
    except Exception as e:
        # Raise a 500 error if the research agent encounters any issues
        raise HTTPException(status_code=500, detail=f"Error running research agent: {str(e)}")