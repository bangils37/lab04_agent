import logging
from typing import Annotated
from typing_extensions import TypedDict
from datetime import datetime

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from tools import calculate_budget, search_flights, search_hotels

load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('conversation.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

tools_list = [search_flights, search_hotels, calculate_budget]
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
llm_with_tools = llm.bind_tools(tools_list)


def agent_node(state: AgentState):
    messages = state["messages"]
    if not messages or not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages

    response = llm_with_tools.invoke(messages)

    if getattr(response, "tool_calls", None):
        for tc in response.tool_calls:
            tool_log = f"Gọi tool: {tc['name']}({tc['args']})"
            print(f"[TOOL] {tool_log}")
            logging.info(f"[TOOL] {tool_log}")
    else:
        print("[INFO] Trả lời trực tiếp")
        logging.info("[INFO] Trả lời trực tiếp")

    return {"messages": [response]}

builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)

tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

graph = builder.compile()

if __name__ == "__main__":
    separator = "=" * 60
    print(separator)
    print("TravelBuddy – Trợ lý Du lịch Thông minh")
    print("      Gõ 'quit' để thoát")
    print(separator)
    
    logging.info(separator)
    logging.info("=== TravelBuddy Agent Started ===")
    logging.info(separator)

    test_count = 0
    while True:
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in ["quit", "exit", "q"]:
            logging.info("=== Session Ended ===")
            break

        test_count += 1
        logging.info(f"\n--- TEST {test_count} ---")
        logging.info(f"User: {user_input}")
        
        print("\nTravelBuddy đang suy nghĩ...")
        result = graph.invoke({"messages": [("human", user_input)]})
        final = result["messages"][-1]
        response_text = final.content
        
        print(f"\nTravelBuddy: {response_text}")
        logging.info(f"Assistant: {response_text}\n")

