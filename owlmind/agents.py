from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from typing import Dict, Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get OpenAI API key from environment or use default for testing
openai_api_key = os.getenv('OPENAI_API_KEY')

class BaseAgent:
    def __init__(self, role: str, system_prompt: str):
        self.llm = ChatOpenAI(
            temperature=0.7,
            model=os.getenv('OPENAI_MODEL', 'gpt-4-turbo-preview'),
            openai_api_key=openai_api_key
        )
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{question}")
        ])
        self.chain = self.prompt | self.llm
        
    def process(self, question: str) -> str:
        response = self.chain.invoke({"question": question})
        return response.content

class QuestionClassifier:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0,
            model=os.getenv('OPENAI_MODEL', 'gpt-4-turbo-preview'),
            openai_api_key=openai_api_key
        )
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a question classifier. Classify the following question into one of these categories:
            - DOUBT_SOLVER: Questions about concepts, explanations, or understanding
            - CODE_REVIEW: Questions about code, programming, or technical implementation
            - STUDY_PLANNER: Questions about learning strategies, study plans, or educational guidance
            
            Return only the category name."""),
            ("human", "{question}")
        ])
        self.chain = self.prompt | self.llm
        
    def classify(self, question: str) -> str:
        response = self.chain.invoke({"question": question})
        return response.content.strip()

class DoubtSolverAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Doubt Solver",
            system_prompt="""You are an expert educator with deep knowledge in various subjects.
            Your goal is to help students understand concepts clearly and solve their doubts
            in a way that promotes deep learning and understanding.
            Provide clear, detailed explanations and examples when appropriate."""
        )

class CodeReviewAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Code Reviewer",
            system_prompt="""You are an experienced software developer and code reviewer.
            Your expertise lies in helping students understand programming concepts,
            debug code, and improve their coding practices.
            Provide practical, actionable advice and code examples when appropriate."""
        )

class StudyPlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Study Planner",
            system_prompt="""You are an expert in educational psychology and learning strategies.
            Your role is to help students create effective study plans, manage their time,
            and develop good learning habits.
            Provide personalized, practical study strategies and time management tips."""
        )

class AgentOrchestrator:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.agents = {
            "DOUBT_SOLVER": DoubtSolverAgent(),
            "CODE_REVIEW": CodeReviewAgent(),
            "STUDY_PLANNER": StudyPlannerAgent()
        }
        
    def get_response(self, question: str) -> str:
        try:
            # Classify the question
            category = self.classifier.classify(question)
            
            # Get the appropriate agent
            agent = self.agents.get(category)
            if not agent:
                return "I'm not sure how to help with this question. Please try rephrasing it."
            
            # Process the question with the selected agent
            return agent.process(question)
            
        except Exception as e:
            return f"An error occurred while processing your question: {str(e)}" 