import os
from dotenv import load_dotenv
from termcolor import colored
from agents.engineer import EngineerAgent
from agents.biologist import BiologistAgent
from agents.analyst import AnalystAgent
from tools.search_tool import SearchTool
from tools.calculator_tool import CalculatorTool

# Load environment variables
load_dotenv()

def test_flow():
    print(colored("Testing Eco-Mime Agent Team...", "green"))
    
    try:
        engineer = EngineerAgent()
        biologist = BiologistAgent()
        analyst = AnalystAgent()
        
        # Initialize Tools
        search_tool = SearchTool()
        calculator_tool = CalculatorTool()
        
        # Inject Tools
        biologist.set_tools(search_tool)
        analyst.set_tools(calculator_tool)
    except ValueError as e:
        print(colored(f"Error: {e}", "red"))
        return

    user_input = "I need a helmet that protects against high-impact collisions for construction workers."
    print(colored(f"\nTest Input: {user_input}", "cyan"))
    
    # 1. Engineer analyzes the problem
    print(colored("\n--- Phase 1: Engineering Analysis ---", "yellow"))
    engineer_response = engineer.send_message(f"User Problem: {user_input}\nAnalyze this problem and identify key mechanical constraints.")
    
    # 2. Biologist finds inspiration
    print(colored("\n--- Phase 2: Biomimicry Research ---", "yellow"))
    biologist_response = biologist.research_and_respond(f"Engineering Problem: {user_input}\nEngineer's Analysis: {engineer_response}\nFind biological systems that solve this.")
    
    # 3. Engineer proposes design
    print(colored("\n--- Phase 3: Design Proposal ---", "yellow"))
    design_proposal = engineer.send_message(f"Biologist's Findings: {biologist_response}\nPropose a detailed mechanical design incorporating these biological insights.")
    
    # 4. Analyst evaluates
    print(colored("\n--- Phase 4: Sustainability Analysis ---", "yellow"))
    analyst_response = analyst.analyze_and_respond(f"Design Proposal: {design_proposal}\nEvaluate the sustainability of this design.")
    
    print(colored("\n--- Test Complete ---", "green"))

if __name__ == "__main__":
    test_flow()
