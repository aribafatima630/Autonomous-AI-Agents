from agents.stateSchema import AgentState
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="openai/gpt-oss-120b",
    temperature=0.3,
    max_tokens=400
)

WRITER_PROMPT = ChatPromptTemplate.from_template(
     """
You are an expert analytical writer.

Using the research notes below, write a clear and structured draft answer
that addresses the user's goal.

Instructions:
- Use only the provided research notes
- Synthesize the information clearly
- Organize with headings or short sections
- Avoid copying notes verbatim
- Ensure the answer is complete
- Do not stop mid sentence

User goal:
{goal}

Research notes:
{research_notes}
"""
)

def writer_node(state: AgentState) -> AgentState:
    """
    Writer node:
    - Takes research notes
    - Produces a structured draft answer
    - Stores it in state["draft_answer"]
    """

    goal = state["goal"]
    research_notes = "\n\n".join(state["research_notes"])

    response = llm.invoke(
        WRITER_PROMPT.format_messages(
            goal=goal,
            research_notes=research_notes
        )
    )

    state["draft_answer"] = response.content.strip()
    state["final_answer"] = state["draft_answer"]

    return state
