# COT_6930_Code_Tarvatha_final_project
# StudyPal: A GenAI-Powered Study Assistant & Productivity Bot

## 📚 Overview
**StudyPal** is an intelligent, Discord-based assistant designed to support students by answering academic doubts, reviewing code, and suggesting personalized study strategies.  
Built using **LangChain**, **OpenAI LLMs**, and **Discord Bot APIs**, StudyPal dynamically classifies user queries and routes them to specialized agents for tailored assistance.

## 🚀 Features
- 🎯 **Query Classification** into Doubt Solving, Code Review, and Study Planning.
- 🤖 **Multi-Agent Orchestration** for modular, task-specific responses.
- 📚 **Educational Support** with clear explanations and practice suggestions.
- 💻 **Code Review Assistance** using Codex models for debugging and best practices.
- 📅 **Study Planning Advice** with time management strategies.
- ⚙️ **Dynamic Prompt Templates** and LLM parameter tuning (temperature, max tokens).
- 🛡️ **Robust Error Handling** with fallback mechanisms.

## 🏗️ Architecture
Student → Discord Bot → AgentOrchestrator → Specialized Agent → OpenAI Model → Response → Student

- **Discord Bot** captures user messages.
- **AgentOrchestrator** classifies and routes queries.
- **DoubtSolverAgent / CodeReviewAgent / StudyPlannerAgent** processes based on category.
- **OpenAI API** provides intelligent completions.

## 🔧 Technologies Used
- **Python 3.10+**
- **LangChain**
- **OpenAI API (gpt-4-turbo-preview)**
- **Discord.py**
- **LangChain-Community Components**
- **Dotenv for Secure API Management**

## 📁 Project Structure

```bash
owlmind/
├── agents.py          # Specialized Agent Definitions (DoubtSolver, CodeReview, StudyPlanner)
├── bot-1.py           # Discord Bot Implementation (Handles incoming user messages)
├── orchestrator.py    # AgentOrchestrator Class (Routes questions to the correct agent)
├── test_agents.py     # Simple Interactive CLI Tester for Agents
├── .env               # Environment Variables (OpenAI API Key, Discord Bot Token)
├── requirements.txt   # Python Dependencies List
└── README.md          # Project Documentation (this file)
```

## ⚡ Setup Instructions
1. **Clone the repository:**
   ```bash
   # Clone the repository
   git clone https://github.com/ptotakura2023/COT_6930_Code_Tarvatha_final_project.git
   # Navigate into the project directory
   cd COT_6930_Code_Tarvatha_final_project
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Configure your environment variables:**
   Create a .env file:
   ```bash
   OPENAI_API_KEY=your-openai-api-key
   DISCORD_BOT_TOKEN=your-discord-bot-token
   OPENAI_MODEL=gpt-4-turbo-preview
4. **Run the bot:**
    ```bash
   python bot-1.py
5. **(Optional) Test Agents Locally:**
   ```bash
   python test_agents.py

## 🎯 Example Interactions
- **User:** "Explain recursion."
- **StudyPal:** Provides a clear, step-by-step explanation with examples.

- **User:** "My Python function has a list index out of range error."
- **StudyPal:** Diagnoses the issue and suggests code fixes.

- **User:** "Help me build a study plan for exams."
- **StudyPal:** Suggests time management techniques and daily goals.

---

## ⚙️ Configurations
**LLM Parameters:**
- **Temperature:** 0.7 (creative but controlled)
- **Top_p:** 0.9
- **Max Tokens:** 2048

**System Prompts:**  
Custom designed for each specialized agent role (Doubt Solver, Code Reviewer, Study Planner) to ensure optimal and context-specific responses.

---

## 🧠 Future Enhancements

- Further enhance the Retrieval Augmented Generation (RAG) mechanisms for even deeper knowledge retrieval and grounding.
- Expand memory-based contextual conversations to support longer, multi-turn user sessions.
- Refine multi-turn dialogue flows and optimize conversation history tracking for personalized user experience.


---

## 🤝 Contributing
Feel free to fork this project and propose improvements!  
Bug fixes, suggestions, and new ideas are always welcome. 🚀

If you'd like to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-xyz`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-xyz`).
5. Open a pull request!

Let's build something amazing together! 💬
