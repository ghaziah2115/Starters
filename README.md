# Starters
# SimpleAgent

A simple AI assistant built using **LangChain**, **LangGraph**, and **OpenAI GPT**.  
It can chat with users, perform reasoning, and can be extended with tools for actions like calculations or web search.


## Features
- Interactive AI chat using ReAct (Reason + Act) framework
- Streaming responses (see the AI type in real-time)
- Easily extendable with custom tools
- Uses environment variables for API keys (kept private)


## Requirements
- Python 3.13 or above
- [OpenAI API key](https://platform.openai.com/account/api-keys)
- Packages:
  - `langchain`
  - `langchain-openai`
  - `langgraph`
  - `python-dotenv`

You can install dependencies using:
```bash
uv add langgraph langchain python-dotenv langchain-openai
