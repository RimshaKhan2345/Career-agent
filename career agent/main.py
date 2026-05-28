import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, result
from agents.run import RunConfig
from Career_agent import get_career_roadmap

load_dotenv()
client = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
model = OpenAIChatCompletionsModel(model="openai/gpt-3.5-turbo", openai_client=client)
config = RunConfig(model=model, tracing_disabled=True)

job_agent = Agent(
    name="JobAgent",
    instructions="You are a job agent that helps users find job opportunities based on their skills and interests.",
    model=model
)

skill_agent = Agent(
    name="SkillAgent",
    instructions="You are a smart skill agent that helps users identify and develop skills needed for their career.",
    model=model,
    tools=[get_career_roadmap],
    handoffs=[job_agent]
)

career_agent = Agent(
    name="CareerAgent",
    instructions="You are career agent you ask about interests and helps users create a personalized career roadmap.",
    model=model,
    handoffs=[skill_agent]
)

async def main():
    print("\U0001F393 Career Mentor Agent\n")
    response = input("What are your interests? ")

    result = await Runner.run(career_agent, response, run_config=config)
    print(f"\n📝 {result.last_agent.name}:")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
    print("\nThank you for using the Career Mentor Agent!")
    print("\nThank you for using the Career Mentor Agent!")
