from typing import Annotated, TypedDict

from langgraph.graph import add_messages


class State(TypedDict):
    messages: Annotated[list, add_messages]
    test_cases: str
    plan: str
    llmtype:str
    model:str

