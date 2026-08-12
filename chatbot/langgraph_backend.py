from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.message import add_messages

load_dotenv()

# llm
llm = ChatOllama(
    model="gpt-oss:120b",
    base_url="https://ollama.com/",
)

# Chat State
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# chat_node function
def chat_node(state: ChatState):

    # take users query from state
    query = state['messages']

    # send query to llm
    response = llm.invoke(query)

    # store response in state
    return {'messages': [response]}

# create nodes, edges and checkpointer

checkpointer = MemorySaver()

graph = StateGraph(ChatState)
graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)