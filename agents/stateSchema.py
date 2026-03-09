from typing import Dict,List,Optional
from typing_extensions import TypedDict

class AgentState(TypedDict):
    #user input
    goal:str

    #planning
    plan:List[str]

    #research over goal
    research_notes:List[str]
    sources:List[str]

    #draft answer
    draft_answer:str

    #checking answer is realiable or not
    critic_notes:Optional[str]
    is_approved:bool

    #number of iteration
    iteration:int
    max_iteration:int

    #final answer
    final_answer:Optional[str]