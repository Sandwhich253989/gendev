from langgraphh.graph_router import construct_graph


def run_req_graph(question, thread_id, llmtype, model):
    graph = construct_graph()

    config = {"configurable": {"thread_id": str(thread_id)}}

    events = graph.stream({"messages": [("user", question)], "llmtype": llmtype, "model": model}, config,
                          stream_mode="values")

    for event in events:
        event["messages"][-1].pretty_print()

    return event["messages"][-1].content
