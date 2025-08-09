from agency_swarm import set_openai_key
from dotenv import load_dotenv
import os
from agency_swarm import Agency
from my_agents import greeter, responder
# Load environment variables from .env file
load_dotenv()
key = os.getenv("OPENAI_API_KEY")
if not key:
    raise ValueError("openai key not found in .env file")
set_openai_key(key)


# Define the agency with the agents and their interactions
# The flows define how agents interact with each other
flows = [
    greeter,
    [greeter, responder],
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

    reply = agency.get_completion(user_message, recipient_agent=greeter)
    print("Swarm:", reply)




