import os
import google.generativeai as genai
from termcolor import colored
from utils.session_manager import SessionManager

class BaseAgent:
    def __init__(self, name, instructions, model_name="gemini-2.0-flash"):
        self.name = name
        self.instructions = instructions
        self.model_name = model_name
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=self.instructions
        )
        
        self.session_manager = SessionManager()
        history = self.session_manager.load_session(self.name)
        # Convert dict history back to content objects if needed, 
        # but genai.start_chat accepts list of dicts with 'role' and 'parts'
        self.chat = self.model.start_chat(history=history)
        if history:
            print(colored(f"[{self.name}]: Resumed session with {len(history)} messages.", "magenta"))

    def save(self):
        self.session_manager.save_session(self.name, self.chat.history)

    def send_message(self, message):
        print(colored(f"\n[User -> {self.name}]: {message}", "cyan"))
        response = self.chat.send_message(message)
        try:
            print(colored(f"[{self.name}]: {response.text}", "green"))
        except UnicodeEncodeError:
            # Fallback for Windows consoles that can't handle some unicode chars
            safe_text = response.text.encode('ascii', 'replace').decode('ascii')
            print(colored(f"[{self.name}]: {safe_text}", "green"))
        return response.text
