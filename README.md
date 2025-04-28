# COT_6930_Code_Tarvatha_final_project
StudyPal: A GenAI-Powered Study Assistant & Productivity Bot
📚 Overview
StudyPal is an intelligent, Discord-based assistant designed to support students by answering academic doubts, reviewing code, and suggesting personalized study strategies.
Built using LangChain, OpenAI LLMs, and Discord Bot APIs, StudyPal dynamically classifies user queries and routes them to specialized agents for tailored assistance.

🚀 Features
🎯 Query Classification into Doubt Solving, Code Review, and Study Planning.

🤖 Multi-Agent Orchestration for modular, task-specific responses.

📚 Educational Support with clear explanations and practice suggestions.

💻 Code Review Assistance using Codex models for debugging and best practices.

📅 Study Planning Advice with time management strategies.

⚙️ Dynamic Prompt Templates and LLM parameter tuning (temperature, max tokens).

🛡️ Robust Error Handling with fallback mechanisms.

🏗️ Architecture
nginx
Copy
Edit
Student → Discord Bot → AgentOrchestrator → Specialized Agent → OpenAI Model → Response → Student
Discord Bot captures user messages.

AgentOrchestrator classifies and routes queries.

DoubtSolverAgent / CodeReviewAgent / StudyPlannerAgent processes based on category.

OpenAI API provides intelligent completions.

🔧 Technologies Used
Python 3.10+

LangChain

OpenAI API (gpt-4-turbo-preview)

Discord.py

LangChain-Community Components

Dotenv for Secure API Management

📂 Project Structure
bash
Copy
Edit
owlmind/
│
├── agents.py          # Specialized Agent Definitions
├── bot-1.py           # Discord Bot Implementation
├── orchestrator.py    # AgentOrchestrator Class
├── test_agents.py     # Simple Interactive Test Script
├── .env               # Environment Variables (OpenAI API Key, Bot Token)
├── requirements.txt   # Python Requirements
└── README.md          # Project Documentation (this file)
⚡ Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/StudyPal-Discord-Bot.git
cd StudyPal-Discord-Bot
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure your environment variables:

Create a .env file:

ini
Copy
Edit
OPENAI_API_KEY=your-openai-api-key
DISCORD_BOT_TOKEN=your-discord-bot-token
OPENAI_MODEL=gpt-4-turbo-preview
Run the bot:

bash
Copy
Edit
python bot-1.py
(Optional) Test Agents Locally:

bash
Copy
Edit
python test_agents.py
🎯 Example Interactions
User: "Explain recursion."

StudyPal: Provides a clear, step-by-step explanation with examples.

User: "My Python function has a list index out of range error."

StudyPal: Diagnoses the issue and suggests code fixes.

User: "Help me build a study plan for exams."

StudyPal: Suggests time management techniques and daily goals.

⚙️ Configurations
LLM Parameters:

Temperature: 0.7 (creative but controlled)

Top_p: 0.9

Max Tokens: 2048

System Prompts designed for specific agent roles.

🧠 Future Enhancements
 Integrate RAG (Retrieval Augmented Generation) for better knowledge grounding.

 Add memory-based contextual conversations.

 Multi-turn conversation flow improvements.

🤝 Contributing
Feel free to fork this project and propose improvements!
Bug fixes and feature suggestions are welcome 🚀
