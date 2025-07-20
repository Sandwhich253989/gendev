from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraphh.context import context_chain
from langgraphh.summary import summarize_chain
from langgraphh.state import State


def generate_node(state):
    return {"messages": context_chain(state["llmtype"], state["model"]).invoke({"messages": state["messages"]})}


def summarize_node(state):
    return {"messages": summarize_chain(state["llmtype",state["model"]]).invoke({"messages": state["messages"]})}


def should_continue(state):
    messages = state["messages"]
    last_message = messages[-1]
    if "FINISHED_CALL" not in last_message.content:
        return "generate_node"
    else:
        return "summary"


def construct_graph():
    memory = SqliteSaver.from_conn_string(r"C:\Users\avane\PycharmProjects\GenDev\sqlite3_db\chat-history.sqlite")

    graph_builder = StateGraph(State)

    graph_builder.add_node("generate", generate_node)
    graph_builder.add_node("summary", summarize_node)

    graph_builder.add_conditional_edges("generate", should_continue, {
        "generate_node": END,
        "summary": "summary"
    })

    graph_builder.add_edge("summary", END)
    graph_builder.set_entry_point("generate")
    graph = graph_builder.compile(checkpointer=memory)
    return graph
