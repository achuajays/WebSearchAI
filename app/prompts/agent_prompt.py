"""
Comprehensive research prompts for LLM agents.

This module provides a class for generating detailed research prompts for LLM agents.
The prompts guide the agent through a systematic research methodology including search,
data extraction, news analysis, and synthesis.

The class is designed to be easy to use and provides clear documentation for each
method and attribute. Code is well-commented and readable.

Example:

    >>> from app.prompts.agent_prompt import AgentPrompt
    >>> agent_prompt = AgentPrompt("your research question or topic")
    >>> prompt = agent_prompt.get_prompt()
    >>> print(prompt)

This will output a comprehensive research prompt with detailed instructions for
conducting research on the provided topic.

"""
class AgentPrompt:
    """
        A class that generates comprehensive research prompts for LLM agents.

        This class creates structured, detailed prompts for conducting thorough
        research on a specified topic. The prompts guide the agent through a
        systematic research methodology including search, data extraction,
        news analysis, and synthesis.

        Attributes:
            query (str): The research topic or question to investigate.
        """
    def __init__(self , query) -> None:
        """
                Initialize the Agent_Prompt with a research query.

                Args:
                    query (str): The topic or question to research.
        """
        self.query = query

    def get_prompt(self) -> str:
        """
                Generate a comprehensive research prompt based on the query.

                The generated prompt includes detailed instructions for:
                - Conducting systematic web searches
                - Extracting and analyzing data from authoritative sources
                - Analyzing recent news coverage
                - Synthesizing findings into a comprehensive research report

                Returns:
                    str: A detailed research prompt with methodology and output requirements.
        """
        prompt = f"""Act as an advanced research agent investigating '{self.query}'.

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
                - Ensure all responses are matched to the research topic
                """

        return prompt