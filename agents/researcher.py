from agents.stateSchema import AgentState
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


llm = ChatOpenAI(
    model="openai/gpt-oss-120b",
    temperature=0,
    max_tokens=300
)


RESEARCHER_PROMPT = ChatPromptTemplate.from_template(
    """
You are a research assistant.

Research the following task carefully and return concise factual notes.

Instructions:
- Provide concise bullet point notes
- Focus only on relevant factual information
- Avoid long paragraphs
- Do not speculate
- Do NOT include long explanations or formulas
- Do not produce a final answer

Research task:
{task}
"""
)


def researcher_node(state: AgentState) -> AgentState:
    """
    Researcher node:
    - Takes each step from the plan
    - Produces research notes
    - Stores findings in state["research_notes"]
    """

    research_notes = []
    sources = []

    for step in state["plan"]:
        response = llm.invoke(
            RESEARCHER_PROMPT.format_messages(task=step)
        )

        research_notes.append(f"{step}:\n{response.content}")
        sources.append("LLM internal knowledge")  # placeholder for now

    state["research_notes"] = research_notes
    state["sources"] = sources

    return state