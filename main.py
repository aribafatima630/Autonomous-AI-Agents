from dotenv import load_dotenv
load_dotenv()

from graph import app
from agents.stateSchema import AgentState

initial_state: AgentState = {
    "goal": "Impact of Generative AI on software engineering jobs",
    "plan": [],
    "research_notes": [],
    "sources": "",
    "draft_answer": "",
    "critic_notes": None,
    "is_approved": False,
    "iteration": 0,
    "max_iteration": 3,
    "final_answer": ""
}

result = app.invoke(initial_state)

print("\n===== DEBUG OUTPUT =====\n")
for key, value in result.items():
    print(f"{key}: {value}\n")