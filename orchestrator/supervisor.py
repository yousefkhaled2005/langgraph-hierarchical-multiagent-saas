# Hierarchical LangGraph State Supervisor
from typing import TypedDict, Annotated, Sequence

class AgentState(TypedDict):
    messages: Sequence[str]
    next_worker: str
    task_approved: bool

def supervisor_router(state: AgentState):
    print("Supervisor evaluating task state. Delegating to specialized subagent.")
    return {"next_worker": "researcher_agent"}
