
from model.llm import llm_model
from state.appState import ChatWithMeState

async def new_chatbot(state):
    messages=await llm_model.ainvoke(state["messages"])
    return {
        "messages":[messages]
        }