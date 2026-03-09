from langgraph.graph import StateGraph, END

from agents.stateSchema import AgentState
from agents.planner import planner_node
from agents.researcher import researcher_node
from agents.writer import writer_node
from agents.critic import critic_node

graph = StateGraph(AgentState)

graph.add_node("planner",planner_node)
graph.add_node("researcher",researcher_node)
graph.add_node("writer",writer_node)
graph.add_node("critic",critic_node)

graph.set_entry_point("planner")

graph.add_edge("planner","researcher")
graph.add_edge("researcher","writer")
graph.add_edge("writer","critic")

def critic_decision(state: AgentState):
    if state["is_approved"]:
        return END
    
    if state["iteration"] >= state["max_iteration"]:
        return END
    
    return "writer"

graph.add_conditional_edges(
    "critic",
    critic_decision,
    {
        "writer": "writer",
        END: END
    }
)

# Compile graph
app = graph.compile()
