
from model.llm import llm_model
from state.appState import ChatWithMeState
from langsmith import traceable

@traceable
async def new_chatbot(state):   
    messages=await llm_model.ainvoke(state["messages"])
    return {
        "messages":[messages]
        }