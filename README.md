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
