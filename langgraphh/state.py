from typing import Annotated, List, TypedDict, Sequence

from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages


class State(TypedDict):
    messages: Annotated[list, add_messages]
    task: str
    plan_string: str
    steps: List
    results: dict
    result: str
    msg: Annotated[list, add_messages]
    llmtype: str
    model: str
