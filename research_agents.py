from agents import Agent, Runner, WebSearchTool
from dotenv import load_dotenv
import os

load_dotenv()

import asyncio

# Define research agents with WebSearchTool
research_agent_1 = Agent(
    name="Research Agent 1",
    instructions="Conduct research using the WebSearchTool.",
    tools=[WebSearchTool()]
)

# Define report writing agent
report_agent = Agent(
    name="Report Agent",
    instructions="Write a report based on the research findings.",
)

# Define triage agent to handoff tasks to research agents and report agent
triage_agent = Agent(
    name="Triage Agent",
    instructions="First, the research agent will conduct their searches. Then, the report agent will compile the findings into a report.",
    handoffs=[research_agent_1, report_agent],
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
