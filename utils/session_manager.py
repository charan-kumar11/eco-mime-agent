import json
import os

class SessionManager:
    def __init__(self, storage_dir="sessions"):
        self.storage_dir = storage_dir
        if not os.path.exists(self.storage_dir):
            os.makedirs(self.storage_dir)

    def save_session(self, agent_name, history):
        """Saves chat history to a JSON file."""
        filename = f"{agent_name.replace(' ', '_').lower()}_session.json"
        filepath = os.path.join(self.storage_dir, filename)
        
        # Convert history objects to serializable format if needed
        # Assuming history is a list of dictionaries or objects with 'role' and 'parts'
        serializable_history = []
        for entry in history:
            # Handle genai.types.Content object or dict
            role = entry.role if hasattr(entry, 'role') else entry.get('role')
            parts = []
            if hasattr(entry, 'parts'):
                for part in entry.parts:
                    parts.append(part.text)
            else:
                parts = entry.get('parts', [])
            
            serializable_history.append({"role": role, "parts": parts})

        with open(filepath, 'w') as f:
            json.dump(serializable_history, f, indent=2)
        print(f"Session saved for {agent_name}")

    def load_session(self, agent_name):
        """Loads chat history from a JSON file."""
        filename = f"{agent_name.replace(' ', '_').lower()}_session.json"
        filepath = os.path.join(self.storage_dir, filename)
        
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                history = json.load(f)
            # Convert back to format expected by genai if necessary
            # For now, returning list of dicts which genai usually accepts
            return history
        return []
