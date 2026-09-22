from langgraph.graph import END, START, StateGraph
from state.appState import ChatWithMeState
from nodes.chatbot import new_chatbot
from langgraph.checkpoint.memory import MemorySaver


async def execute_graph():

    builder=StateGraph(ChatWithMeState)

    #adding nodes

    builder.add_node("chatbot_node",new_chatbot)


    #adding edges
    builder.add_edge(START,"chatbot_node")
    builder.add_edge("chatbot_node",END)

    memory= MemorySaver()
    config= {'configurable':{
        'thread_id':1
    }}

    #complie the builder

    graph=builder.compile(memory)

    while True:
        prompt=input("Me: ")
        if prompt in {"bye","exit","thank you"}:
            result=await graph.ainvoke({
                "messages":{
                    "role":"user",
                    "content":prompt
                }
            },config=config)
            print(result["messages"][-1].content)
            break;
        else:
            result=await graph.ainvoke({
                        "messages":{
                            "role":"user",
                            "content":prompt
                        }
                    },config=config)
        print("ChatWithMeBot: ",result["messages"][-1].content)
        print("\n")




