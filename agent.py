# from langchain_openai import AzureChatOpenAI
# from browser_use import Agent
# from pydantic import SecretStr
# import os

# # Initialize the model
# llm = AzureChatOpenAI(
#     model="gpt-4o",
#     api_version='2024-02-01',
#     azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
#     api_key=os.getenv('AZURE_OPENAI_KEY', ''),
# )

# # Create agent with the model
# agent = Agent(
#     task="Go to google.com and search for 'LangChain'.",
#     llm=llm
# )
import asyncio
import logging
from langchain_openai import AzureChatOpenAI
from browser_use import Agent
import os

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Initialize the model
llm = AzureChatOpenAI(
    model="gpt-4o-mini",
    api_version='2024-02-01',
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
    api_key=os.getenv('AZURE_OPENAI_KEY', ''),
)

# Create agent with the model
agent = Agent(
    task="Go to google and search for 'langchain'.",
    llm=llm
)

# Run the agent asynchronously
async def main():
    response = await agent.run()
    print(response)

asyncio.run(main())  # Run the async function


