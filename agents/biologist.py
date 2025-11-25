from .base_agent import BaseAgent
from termcolor import colored

class BiologistAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="The Biologist",
            instructions="""You are an expert Biologist specializing in Biomimicry.
            Your goal is to find biological systems that solve problems similar to the engineering challenges presented.
            When the Engineer presents a problem (e.g., 'cooling a building'), you search for how nature solves it (e.g., 'termite mounds', 'elephant ears', 'human skin').
            Explain the biological mechanism clearly so the Engineer can apply it."""
        )
        self.search_tool = None

    def set_tools(self, search_tool):
        self.search_tool = search_tool

    def research_and_respond(self, message):
        # 1. Extract search query from message (simplified)
        # In a real app, we'd ask the LLM to generate the query.
        # For now, we'll just append "biomimicry" to the message for the search.
        search_query = f"{message} biomimicry nature solutions"
        
        print(colored(f"[{self.name}]: Searching for '{search_query}'...", "blue"))
        search_results = ""
        if self.search_tool:
            search_results = self.search_tool.search(search_query)
        
        # 2. Feed results to LLM
        context = f"Search Results:\n{search_results}\n\nUser Message: {message}"
        return self.send_message(context)
