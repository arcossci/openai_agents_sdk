from agents import Agent, Runner, WebSearchTool
from dotenv import load_dotenv
import os

load_dotenv()

import asyncio

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You only speak Spanish.",
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[spanish_agent, english_agent],
)


async def main():
    while True:
        user_input = input("Enter your message (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        result = await Runner.run(triage_agent, input=user_input)
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
