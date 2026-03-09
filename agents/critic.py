from agents.stateSchema import AgentState
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model = "openai/gpt-oss-120b",
    temperature = 0,
    max_tokens=250
)

CRITIC_PROMPT = ChatPromptTemplate.from_template(
    """
You are a strict AI reviewer.

Your task:
- Review the draft answer
- Verify it strictly against the research notes
- Identify hallucinations, inaccuracies, or missing key points

Rules:
- Use ONLY the research notes for verification
- If the draft contains information not supported by research notes, mark it as an issue
- Be concise and specific
- Decide clearly if the draft is acceptable

Return your response in the following format:

Decision: APPROVED or REJECTED
Critic Notes:
- Bullet point feedback

User Goal:
{goal}

Research Notes:
{research_notes}

Draft Answer:
{draft_answer}
"""
)

def critic_node(state: AgentState) -> AgentState:
    """
    Critic node:
    - Reviews the draft answer
    - Produces feedback
    - Approves or rejects the draft
    - Controls iteration count
    """

    goal = state["goal"]
    research_notes = "\n\n".join(state["research_notes"])
    draft_answer = state["draft_answer"]

    response = llm.invoke(
        CRITIC_PROMPT.format_messages(
            goal = goal,
            research_notes=research_notes,
            draft_answer=draft_answer
        )
    )
    
    content = response.content.strip()

    state["critic_notes"] = content

    if content.startswith("Decision: APPROVED"):
        state["is_approved"] = True
    else:
        state["is_approved"] = False
        state["iteration"] += 1

    return state
