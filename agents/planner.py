from agents.stateSchema import AgentState
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os 

llm = ChatOpenAI(
    model = "openai/gpt-oss-120b",
    temperature = 0,
    max_tokens=200
)

PLANNER_PROMPT = ChatPromptTemplate.from_template(
    """
You are an expert research planner.

Your task is to break the user's goal into clear, logical research steps.

Rules:
- Create a concise research plan with 3–4 steps maximum.
- Each step should be concise
- Steps should be actionable
- Do NOT explain anything

User goal:
{goal}
"""
)

def planner_node(state: AgentState) -> AgentState:
     
    """
    Planner node:
    - Takes user goal
    - Generates a step-by-step research plan
    - Stores it in state["plan"]
    """

    goal = state["goal"]

    response = llm.invoke(
        PLANNER_PROMPT.format_messages(goal=goal)
        )
    
    steps = [
        line.strip()
        for line in response.content.split("\n")
        if line.strip()
    ]

    state["plan"] = steps if steps else ["Research the topic broadly"]

    return state
