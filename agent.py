from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search
from google.genai import types
import asyncio

APP_NAME="google_search_agent"
USER_ID="user1234"
SESSION_ID="1234"

root_agent = Agent(
    model='gemini-2.5-flash',
    name='basic_search_agent',
    description='Agent to answer questions using Google Search.',
    instruction="""
    You are a helpful assistant with access to Google Search.
    
    If the user asks a question that requires current information or facts, use the 'google_search' tool.
    Always cite your sources implicitly by providing the answer clearly based on the search results.
    """,
    # google_search is a pre-built tool which allows the agent to perform Google searche.
    tools=[google_search],
)

# Session and Runner
async def setup_session_and_runner():
    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    runner = Runner(session_service=session_service, agent=root_agent, app_name=APP_NAME)
    return session, runner

# Agent Interaction
async def call_agent_async(query):
    content = types.Content(role='user', parts=[types.Part(text=query)])
    session, runner = await setup_session_and_runner()
    events = runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    async for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text
            print("Agent Response:", final_response)

if __name__ == "__main__":
    asyncio.run(call_agent_async("What is the current population of New York City?"))
