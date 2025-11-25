# Eco-Mime: The Biomimicry Engineering Agent
## Google AI Agents Capstone Project - Agents for Good Track

### 1. Problem & Solution Pitch
**Problem:**
Sustainable engineering is complex. Engineers often struggle to find materials and designs that are both structurally sound and environmentally friendly. While nature has solved many of these problems over millions of years (biomimicry), bridging the gap between biological research and mechanical engineering is difficult and time-consuming.

**Solution:**
**Eco-Mime** is a multi-agent AI system that acts as an interdisciplinary design team. It automates the process of:
1.  **Analyzing** engineering constraints (The Engineer).
2.  **Researching** biological solutions in nature (The Biologist).
3.  **Evaluating** the sustainability impact of the proposed design (The Analyst).

This agent empowers engineers to create "nature-backed" designs that are efficient, strong, and sustainable by default.

---

### 2. Key Concepts Implemented
This project demonstrates three core AI Agent concepts:

#### A. Multi-Agent System (Role-Based Collaboration)
We implemented three distinct agents, each with a specific persona and goal:
*   **The Engineer**: Focuses on load, stress, and mechanical constraints.
*   **The Biologist**: Focuses on nature's solutions (e.g., "How does a woodpecker avoid brain damage?").
*   **The Analyst**: Focuses on carbon footprint and material sustainability.
*   *Why?* This separation of concerns ensures expert-level focus on each aspect of the problem, mimicking a real-world design firm.

#### B. Tool Use (MCP & Custom Tools)
The agents are equipped with functional tools to ground their reasoning in reality:
*   **Google Search Tool**: Used by the Biologist to find real-world biological examples (e.g., searching for "impact resistance in nature").
*   **Sustainability Calculator**: A custom Python tool used by the Analyst to estimate carbon emissions based on material weight and type.

#### C. Sessions & Memory
The system utilizes a `SessionManager` to persist the conversation history of each agent.
*   *Why?* Engineering projects happen over time. This allows the user to pause, close the application, and resume the design process later without losing context.

---

### 3. Value Proposition
*   **Innovation**: Introduces novel, bio-inspired ideas that a human engineer might not consider.
*   **Efficiency**: Automates the research phase, reducing hours of literature review to seconds.
*   **Sustainability**: Embeds environmental impact analysis directly into the design loop, preventing "greenwashing."

### 4. How to Run
1.  Clone the repository.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Add your API Key to `.env`.
4.  Run the agent: `python main.py`

### 5. Example Workflow
*   **User**: "I need a shock-absorbing helmet for construction workers."
*   **Engineer**: Identifies impact force and weight constraints.
*   **Biologist**: Suggests the **Woodpecker's skull** (spongy bone structure) and **Ram's horns** (spiral geometry).
*   **Engineer**: Proposes a helmet with a honeycomb internal liner and spiral outer ridges.
*   **Analyst**: Calculates the carbon footprint of using recycled polycarbonate vs. bio-foam.
