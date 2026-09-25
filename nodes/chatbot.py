
from model.llm import llm_model
from state.appState import ChatWithMeState
from langsmith import traceable
from langchain.agents import create_agent
from mcpClient.client import MCP_Client
from langchain.agents.middleware import HumanInTheLoopMiddleware

@traceable
async def new_chatbot(state):   
    # messages=await llm_model.ainvoke(state["messages"])
    tools=await MCP_Client.get_tools()
    agent=create_agent(llm_model,tools=tools)
    # print("state(messages) are ---- ",state["messages"])
    result=await agent.ainvoke({
        "messages":state["messages"]
    })
    # new_messages = result["messages"][len(state["messages"]):]
    new_messages = result["messages"]
    # print("Result is : ---------",new_messages)
    return {
        "messages": new_messages
        }