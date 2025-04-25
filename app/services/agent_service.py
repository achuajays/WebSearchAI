"""
Research Agent Service

This module provides a service for running a research agent to investigate a given query.

The service is designed to be used as a singleton, with a single instance created and cached
using the `lru_cache` decorator. This ensures that the agent is only created once, and that
subsequent calls to the service will reuse the same instance.

The service provides a single method, `run_research`, which takes a query string as input and
returns a dictionary containing the research results. The dictionary will have two keys:

* `research_data`: a string containing the compiled research findings
* `resource_links`: a list of strings containing links to sources used in the research

The service uses the `AgentPrompt` class to generate a prompt for the research agent, based on
the input query. The prompt is then passed to the `run` method of the agent, which returns a
dictionary containing the research results.

The service also provides some basic error handling, catching any exceptions raised by the agent
and returning a structured error response.
"""

import json
import os
from typing import Dict, Any, List
from functools import lru_cache
from dotenv import load_dotenv
from app.agents.agent_research import create_research_agent
from app.prompts.agent_prompt import AgentPrompt
from app.utils import config
# Load environment variables
load_dotenv()
class ResearchAgentService:
    """
    A service for running a research agent to investigate a given query.

    The service is designed to be used as a singleton, with a single instance created and cached
    using the `lru_cache` decorator. This ensures that the agent is only created once, and that
    subsequent calls to the service will reuse the same instance.
    """

    def __init__(self) -> None:
        """
        Initialize the service.

        This method is only called once, when the service is first created. It sets up the
        research agent and caches it for subsequent use.
        """
        # Get the API key from environment variables
        self.serper_api_key = config.SERPER_API_KEY
        self.openai_api_key = config.GEMINI_API_KEY

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

        Raises:
            Exception: If the agent raises an exception
        """
        # Run the research agent
        prompt = AgentPrompt(query)
        task = prompt.get_prompt()

        try:
            result = self.agent.run(json.dumps(task))

            # Process the result into the expected format
            if isinstance(result, dict):
                data = result
            else:
                # Try to parse the result as JSON if it's not already a dict
                try:
                    data = json.loads(result)
                except (json.JSONDecodeError, TypeError):
                    # If parsing fails, create a structured response
                    data = {
                        "research_data": str(result),
                        "resource_links": []
                    }

            # Ensure the result has the expected structure and keys
            if not isinstance(data, dict):
                data = {"research_data": str(data), "resource_links": []}

            # Add missing keys with default values
            data.setdefault("research_data", "")
            data.setdefault("resource_links", [])

            return data

        except Exception as e:
            # Log the error for debugging
            logging.error(f"Research agent error: {str(e)}", exc_info=True)

            # Return a structured error response
            return {
                "research_data": f"Error running research agent: {str(e)}",
                "resource_links": []
            }


@lru_cache()
def get_research_agent_service() -> ResearchAgentService:
    """
    Factory function to get a cached instance of ResearchAgentService.
    This ensures we only create one instance of the agent.
    """
    return ResearchAgentService()