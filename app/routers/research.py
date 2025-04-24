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
    query: str


class ResearchResponse(BaseModel):
    research_data: str
    resource_links: List[str]


@router.post("/run", response_model=Dict[str, Any])
async def run_research_agent(
        request: ResearchRequest,
        agent_service=Depends(get_research_agent_service)
):
    """
    Run the research agent to investigate the provided query
    """
    try:
        result = agent_service.run_research(request.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running research agent: {str(e)}")