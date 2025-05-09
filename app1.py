from langchain_ollama import ChatOllama
from browser_use import Agent
import asyncio



async def main():
    agent = Agent(
        task="Go to google, search for youtube, click on youtube and open it",
        llm=ChatOllama(model="qwen2.5")

    )
    result = await agent.run()
    print(result)

# Use await directly in a Jupyter notebook or async environment
asyncio.run(main())