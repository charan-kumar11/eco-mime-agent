from .base_agent import BaseAgent
from termcolor import colored

class AnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="The Analyst",
            instructions="""You are an expert Sustainability Analyst.
            Your goal is to evaluate the environmental impact of the designs proposed by the Engineer and Biologist.
            You should estimate carbon footprint, recyclability, and energy efficiency.
            Provide a 'Sustainability Score' (0-100) and recommendations for improvement."""
        )
        self.calculator_tool = None

    def set_tools(self, calculator_tool):
        self.calculator_tool = calculator_tool

    def analyze_and_respond(self, message):
        # 1. Identify materials (simplified keyword matching)
        materials = ["steel", "aluminum", "concrete", "wood", "plastic", "glass"]
        found_materials = []
        for mat in materials:
            if mat in message.lower():
                found_materials.append(mat)
        
        calc_results = []
        if self.calculator_tool and found_materials:
            print(colored(f"[{self.name}]: Calculating impact for {found_materials}...", "blue"))
            for mat in found_materials:
                # Assuming 100kg for estimation purposes
                result = self.calculator_tool.calculate_impact(mat, 100)
                calc_results.append(str(result))
        
        # 2. Feed results to LLM
        context = f"Calculator Data (Est. 100kg):\n{'; '.join(calc_results)}\n\nDesign Proposal: {message}"
        return self.send_message(context)
