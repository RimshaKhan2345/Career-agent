import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from Career_agent import get_career_roadmap

load_dotenv()
client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)
config = RunConfig(model=model, tracing_disabled=True)

career_agent = Agent(
    name="CareerAgent",
    instructions="You are career agent you ask about interests and helps users create a personalized career roadmap.",
    model=model
)
skill_agent = Agent(
    name="SkillAgent",
    instructions="You are a smart skill agent that helps users identify and develop skills needed for their career.",
    model=model,
    tools=[get_career_roadmap]
)

job_agent = Agent(
    name="JobAgent",
    instructions="You are a job agent that helps users find job opportunities based on their skills and interests.",
    model=model
)

def main():
    print("\U0001F393 Career Mentor Agent\n")
    interest = input("What are your interests? ")

    result1 = Runner.run_sync(career_agent, interest, run_config=config)
    field = result1.final_output.strip()
    print("\n📝 Suggested Career:", field)

    result2 = Runner.run_sync(skill_agent, field, run_config=config)
    print("\n📇 Required Skills:", result2.final_output)

    result3 = Runner.run_sync(job_agent, field, run_config=config)
    print("\n👜 Job Opportunities:", result3.final_output)

if __name__ == "__main__":
    main()
    print("\nThank you for using the Career Mentor Agent!")