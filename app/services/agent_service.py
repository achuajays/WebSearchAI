import json
import os
from typing import Dict, Any, List
from functools import lru_cache
from dotenv import load_dotenv
from app.agents.agent_research import create_research_agent

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
        task = f"""Act as an advanced research agent investigating '{query}'.

        ## OBJECTIVE:
        Produce comprehensive, factually accurate, and well-structured research data on the topic. and if no query just say 
        No Topic Mentioned' dont found and return answer

        ## RESEARCH METHODOLOGY:
        1. INITIAL SEARCH:
           - Conduct systematic web searches to identify authoritative sources
           - Locate precise URLs of relevant web pages (minimum 3-5 high-quality sources)
           - Prioritize academic, governmental, established news, and expert resources
           - Document all sources with complete citation information

        2. DATA EXTRACTION PROCESS:
           - Extract primary content from each URL via web crawling
           - Document key data points, statistics, and factual information
           - Preserve chronology and context of events/developments
           - Note contradictions or disagreements between sources

        3. NEWS ANALYSIS:
           - Extract recent news (within 6 months when applicable)
           - Differentiate between reporting and opinion/editorial content
           - Compare coverage across multiple news sources to identify consensus and divergence
           - Track timeline of developments to establish causal relationships

        4. SYNTHESIS AND ANALYSIS:
           - Organize findings into coherent thematic sections
           - Construct detailed paragraphs (minimum 8-10) that explore each aspect thoroughly
           - Identify patterns, trends, and significant relationships between data points
           - Address counterarguments and alternative perspectives
           - Distinguish between established facts, emerging research, and speculative content

        ## OUTPUT REQUIREMENTS:
        - Begin with an executive summary (250-300 words)
        - Include section headings that create a logical information hierarchy
        - Provide in-depth analysis with minimum 2000 words total content
        - Maintain neutral, objective tone throughout
        - Conclude with 'Research Limitations' section identifying potential gaps
        - Append complete bibliography with all sources in Chicago or APA format

        ## QUALITY CONTROL:
        - Verify all statistical claims against original sources
        - Cross-reference key facts across multiple sources
        - Flag information gaps or areas requiring additional research
        - Ensure all claims are properly attributed
        """

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