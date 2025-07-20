from langgraph.graph import StateGraph, END
from agents.project_manager.prompt import get_plan
from agents.project_manager.state import State
from configs import config

import re


def plan_node(state: State):
    chain = get_plan(state["llmtype"],state["model"])
    task = state["messages"]
    result = chain.invoke({"task": task})
    # result.pretty_print()
    return {"plan_string": result.content, "messages": result.content}


def construct_graph():
    graph_builder = StateGraph(State)

    graph_builder.add_node("plan", plan_node)
    graph_builder.set_entry_point("plan")

    graph = graph_builder.compile()
    return graph
