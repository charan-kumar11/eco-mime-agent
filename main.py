import os
import sys
from dotenv import load_dotenv
from termcolor import colored
from agents.engineer import EngineerAgent
from agents.biologist import BiologistAgent
from agents.analyst import AnalystAgent
from tools.search_tool import SearchTool
from tools.calculator_tool import CalculatorTool

# Load environment variables
load_dotenv()

def main():
    print(colored("Initializing Eco-Mime Agent Team...", "green"))
    
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
        print("Please ensure GEMINI_API_KEY is set in your .env file or environment variables.")
        return

    print(colored("Team Ready! Describe your engineering challenge.", "green"))
    
    while True:
        user_input = input(colored("\nYou: ", "cyan"))
        if user_input.lower() in ['exit', 'quit']:
            print(colored("Saving sessions and exiting...", "magenta"))
            engineer.save()
            biologist.save()
            analyst.save()
            break
            
        # 1. Engineer analyzes the problem
        print(colored("\n--- Phase 1: Engineering Analysis ---", "yellow"))
        engineer_response = engineer.send_message(f"User Problem: {user_input}\nAnalyze this problem and identify key mechanical constraints.")
        
        # 2. Biologist finds inspiration
        print(colored("\n--- Phase 2: Biomimicry Research ---", "yellow"))
        # Use the new research_and_respond method
        biologist_response = biologist.research_and_respond(f"Engineering Problem: {user_input}\nEngineer's Analysis: {engineer_response}\nFind biological systems that solve this.")
        
        # 3. Engineer proposes design
        print(colored("\n--- Phase 3: Design Proposal ---", "yellow"))
        design_proposal = engineer.send_message(f"Biologist's Findings: {biologist_response}\nPropose a detailed mechanical design incorporating these biological insights.")
        
        # 4. Analyst evaluates
        print(colored("\n--- Phase 4: Sustainability Analysis ---", "yellow"))
        # Use the new analyze_and_respond method
        analyst_response = analyst.analyze_and_respond(f"Design Proposal: {design_proposal}\nEvaluate the sustainability of this design.")
        
        print(colored("\n--- Final Report ---", "magenta"))
        print(f"Design: {design_proposal}\n\nSustainability: {analyst_response}")

if __name__ == "__main__":
    main()
