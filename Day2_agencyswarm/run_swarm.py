from agency_swarm import set_openai_key
from dotenv import load_dotenv
import os
from agency_swarm import Agency
from my_agents import greeter, responder, summarizer

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
if not key:
    raise ValueError("OpenAI API key not found in .env file")
set_openai_key(key)


flows = [
    greeter,
    [greeter, summarizer],  # greeter goes straight to summarizer
    [summarizer, responder],
    [responder, greeter],
]
agency = Agency(
    flows,
    shared_instructions="",
    temperature=0.3,
)

print("Swarm is running...Type 'exit' to stop.")
while True:
    user_message = input("You: ")
    if user_message.lower() == "exit":
        print("Exiting the swarm.")
        break
    # If user explicitly asks to summarize, call summarizer directly:
    if "summarize" in user_message.lower() or user_message.lower().startswith("/sum"):
        reply = agency.get_completion(user_message, recipient_agent=summarizer)
        print("Summarizer:", reply)
        continue

    reply = agency.get_completion(user_message, recipient_agent=greeter)
    print("Swarm:", reply)