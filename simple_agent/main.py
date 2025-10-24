from langchain_core.messages import HumanMessage 
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv 

load_dotenv() #this function load variables from .env file into program 

def main():
    model = ChatOpenAI(temperature=0) #using OpenAI LLM / Temperature = 0 means that there is no randomness ... model must be accurate , and focused

    # tools will be mentioned here which our AI agent uses. variable initialized with list
    tools = []

    # create_react_agent : this is the helper in langGraph (pre-built agent framework). It creates AI agent that works on ReAct (reason + act) framework. AI agnet can use model ( LLM ) and tools mentioned.
    agent_executor = create_react_agent(model , tools)

    print("Welcome! I am your Assitant. How can I help you? Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me. ")

   
    while True: 
        user_input = input("\nYou: ").strip() #strip removes trailing white spaces

        if user_input == "quit": 
            break

        print("\nAssistant: " , end="")

         #.stream : generate output gradually word by word 
         # HumanMessage : is a class from LangChain, and it stores who sent the message and content=user_input receives the cointent that user type in terminal
         # sending input to agent 
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ): #getting response from agent
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()
     
