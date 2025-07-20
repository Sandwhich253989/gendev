from typing import Annotated, TypedDict

from langgraph.graph import add_messages


class State(TypedDict):
    messages: Annotated[list, add_messages]
    code: Annotated[list, add_messages]
    brd: str
    llmtype: str
    model: str
