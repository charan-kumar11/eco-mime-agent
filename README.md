# Eco-Mime: The Biomimicry Engineering Agent
## Google AI Agents Capstone Project - Agents for Good Track

**Eco-Mime** is a multi-agent system designed to help mechanical engineers create sustainable, nature-inspired designs. It combines engineering analysis, biomimicry research, and sustainability impact assessment.

### The Team
1.  **The Engineer**: Analyzes mechanical constraints and proposes designs.
2.  **The Biologist**: Searches for biological systems that solve similar problems (Biomimicry).
3.  **The Analyst**: Calculates sustainability metrics (Carbon Footprint).

### Key Concepts Implemented
-   **Multi-Agent System**: Three specialized agents collaborating.
-   **Tools**: Google Search (for research) and Custom Calculator (for sustainability).
-   **Sessions & Memory**: Persists agent context across sessions using `SessionManager`.

### Setup
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Set up your Google Gemini API Key in a `.env` file:
    ```
    GEMINI_API_KEY=your_api_key_here
    ```

### Usage
Run the interactive agent team:
```bash
python main.py
```

Run the automated test flow:
```bash
python test_agent.py
```
