from langgraph.graph import StateGraph, END  # Import StateGraph class and END constant from langgraph.graph
from langgraph.prebuilt import ToolNode  # Import ToolNode from langgraph.prebuilt
from agents.dev_agent.state import State  # Import State class from agents.dev_agent.state
from agents.dev_agent.functions import generate_chain, tools  # Import generate_chain function and tools list


# Function to generate a node in the state graph based on the current state
def generate_node(state: State):
    # Invoke the generate_chain function with messages and BRD from the state
    return {
        "messages": generate_chain(state["llmtype"], state["model"]).invoke(
            {"messages": state["messages"], "brd": state["brd"]}),
        "code": state["messages"]  # Return the current state's messages as code
    }


# Initialize a ToolNode with the tools imported earlier
tool_node = ToolNode(tools)


# Function to route the state based on its content
def _route(state: State):
    messages = state["messages"]
    last_message = messages[-1]  # Get the last message from the messages list in state

    if last_message.tool_calls:  # Check if there are tool calls in the last message
        return "tool"  # Route to the tool node if there are tool calls
    elif "FINAL ANSWER" in last_message.content:  # Check if "FINAL ANSWER" is in the last message content
        return END  # End the process if "FINAL ANSWER" is found
    else:
        return "generate"  # Default route to generate node if neither condition is met


# Function to create and compile the state graph
def create_graph():
    graph_builder = StateGraph(State)  # Initialize StateGraph with the State class

    # Add nodes to the graph builder
    graph_builder.add_node("generate", generate_node)  # Add generate_node function as "generate" node
    graph_builder.add_node("tool", tool_node)  # Add tool_node as "tool" node

    # Set the entry point of the graph to "generate"
    graph_builder.set_entry_point("generate")

    # Add conditional edges based on the _route function
    graph_builder.add_conditional_edges("generate", _route)

    # Add a direct edge from "tool" to "generate"
    graph_builder.add_edge("tool", "generate")

    # Compile and return the compiled state graph
    graph = graph_builder.compile()
    return graph
