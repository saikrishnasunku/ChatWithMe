# from langgraph.graph import StateGraph
from typing import TypedDict,Annotated

from langgraph.graph import add_messages


class ChatWithMeState(TypedDict,total=False):
    messages:Annotated[list,add_messages]