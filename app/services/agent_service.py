import json
import os
from typing import Dict, Any, List
from functools import lru_cache
from dotenv import load_dotenv
from app.agents.agent_research import create_research_agent
from app.prompts.agent_prompt import Agent_Prompt
# Load environment variables
load_dotenv()


class ResearchAgentService:
    def __init__(self):
        # Get the API key from environment variables
        self.serper_api_key = os.getenv("SERPER_API_KEY")
        self.openai_api_key = os.getenv("GEMINI_API_KEY")

        # Initialize the research agent
        self.agent = create_research_agent(
            model_name="gemini/gemini-2.0-flash",
            temperature=0.2,
            serper_api_key=self.serper_api_key,
            max_token=8000
        )

    def run_research(self, query: str) -> Dict[str, Any]:
        """
        Run the research agent to investigate the provided query.

        Args:
            query (str): The topic to research

        Returns:
            Dict[str, Any]: Research results including research_data and resource_links
        """

        # Run the research agent
        prompt = Agent_Prompt(query)
        task = prompt.get_prompt()

        try:
            result = self.agent.run(json.dumps(task))

            # Try to parse the result as JSON
            try:
                data = json.loads(result)
            except json.JSONDecodeError:
                # If the result is not valid JSON, create a structured response
                data = {
                    "research_data": result,
                    "resource_links": []
                }

            # Ensure the result has the expected structure
            if not isinstance(data, dict):
                data = {
                    "research_data": str(data),
                    "resource_links": []
                }
            if isinstance(data , dict):
                data = data

            # Ensure the result has the expected keys
            if "research_data" not in data:
                data["research_data"] = ""
            if "resource_links" not in data:
                data["resource_links"] = []

            return data

        except Exception as e:
            # Handle any errors
            error_message = f"Error running research agent: {str(e)}"
            return {
                "research_data": error_message,
                "resource_links": []
            }


@lru_cache()
def get_research_agent_service() -> ResearchAgentService:
    """
    Factory function to get a cached instance of ResearchAgentService.
    This ensures we only create one instance of the agent.
    """
    return ResearchAgentService()