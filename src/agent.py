"""Simple LangGraph agent example."""
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator

class State(TypedDict):
    messages: Annotated[list, operator.add]

def agent_node(state: State):
    """Simple agent node that echoes messages."""
    last_message = state["messages"][-1] if state["messages"] else {"role": "user", "content": "Hello"}
    response = {
        "role": "assistant",
        "content": f"Echo: {last_message.get('content', '')}"
    }
    return {"messages": [response]}

# Create the graph
graph = StateGraph(State)
graph.add_node("agent", agent_node)
graph.set_entry_point("agent")
graph.add_edge("agent", END)

# Compile the graph
graph = graph.compile()
