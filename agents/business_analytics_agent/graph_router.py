from langgraph.graph import StateGraph, END
from agents.business_analytics_agent.prompt import brd_chain
from agents.business_analytics_agent.state import State


def brd_node(state: State):
    return {"messages": brd_chain().invoke({"messages": state["messages"]})}


def construct_graph():
    graph_builder = StateGraph(State)

    graph_builder.add_node("brd", brd_node)
    graph_builder.set_entry_point("brd")
    graph_builder.add_edge("brd", END)
    graph = graph_builder.compile()
    return graph
