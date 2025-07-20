from langgraph.graph import StateGraph, END
from agents.QA_agent.prompt import get_test_case
from agents.QA_agent.state import State
from configs import config


def test_case_node(state: State):
    chain = get_test_case(state["llmtype"], state["model"])
    test_cases = chain.invoke({"plan": state["plan"]})
    return {"test_cases": test_cases, "messages": test_cases}


def construct_graph():
    graph_builder = StateGraph(State)
    graph_builder.add_node("test_case", test_case_node)
    graph_builder.set_entry_point("test_case")
    graph = graph_builder.compile()
    return graph
