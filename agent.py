import logging
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

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

# Read system prompt
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()
logging.info("✅ System prompt loaded")

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite-preview",
    temperature=0
)
logging.info("✅ LLM initialized (Gemini 3.1 Flash Lite)")

# Define tools
tools_list = [search_flights, search_hotels, calculate_budget]
logging.info(f"✅ {len(tools_list)} tools registered: {[tool.name for tool in tools_list]}")

# Create ReAct Agent
graph = create_agent(
    model=llm,
    tools=tools_list,
    system_prompt=SYSTEM_PROMPT
)
logging.info("✅ ReAct Agent created successfully")

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
        logging.info(f"\n{'='*60}")
        logging.info(f"TEST #{test_count}")
        logging.info(f"{'='*60}")
        logging.info(f"User Input: {user_input}")
        
        print("\nTravelBuddy đang suy nghĩ...")
        logging.info("⏳ Agent processing request...")
        
        result = graph.invoke({"messages": [("human", user_input)]})
        final = result["messages"][-1]

        if isinstance(final.content, list):
            response_text = "\n".join(
                block.get("text", "")
                for block in final.content
                if block.get("type") == "text"
            )
        else:
            response_text = final.content      
              
        logging.info(f"✅ Agent response generated")
        print(f"\nTravelBuddy: {response_text}")
        logging.info(f"Agent Response:\n{response_text}")
        logging.info(f"{'='*60}\n")

