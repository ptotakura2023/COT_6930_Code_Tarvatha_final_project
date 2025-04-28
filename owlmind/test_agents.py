from agents import AgentOrchestrator
import os
from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize the agent orchestrator
    orchestrator = AgentOrchestrator()
    
    print("Welcome to OwlMind Agent Testing Interface!")
    print("Type 'exit' to quit")
    print("-" * 50)
    
    while True:
        try:
            # Get user input
            question = input("\nEnter your question: ").strip()
            
            # Check for exit command
            if question.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
                
            if not question:
                print("Please enter a valid question.")
                continue
                
            # Get response from the agent orchestrator
            print("\nAnalyzing your question...")
            
            # First, get the classification
            category = orchestrator.classifier.classify(question)
            
            # Display which agent is handling the question
            agent_roles = {
                "DOUBT_SOLVER": "Doubt Solver Agent",
                "CODE_REVIEW": "Code Review Agent",
                "STUDY_PLANNER": "Study Planner Agent"
            }
            
            agent_role = agent_roles.get(category, "Unknown Agent")
            print(f"\nQuestion assigned to: {agent_role}")
            
            # Explain why this agent was chosen
            classification_reasons = {
                "DOUBT_SOLVER": "This question appears to be about understanding concepts or seeking explanations.",
                "CODE_REVIEW": "This question seems to be related to programming, code, or technical implementation.",
                "STUDY_PLANNER": "This question appears to be about learning strategies or study planning."
            }
            
            print(f"Reason: {classification_reasons.get(category, 'The question could not be clearly categorized.')}")
            print("\nProcessing response...")
            
            # Get and display the response
            response = orchestrator.get_response(question)
            
            print("\nResponse:")
            print("-" * 50)
            print(response)
            print("-" * 50)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    main() 