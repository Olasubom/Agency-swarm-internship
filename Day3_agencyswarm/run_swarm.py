from agency_swarm import set_openai_key
from dotenv import load_dotenv
import os
from agency_swarm import Agency
from my_agents import greeter, responder, summarizer, router

load_dotenv()
key = os.getenv("OPENAI_API_KEY")
if not key:
    raise ValueError("OpenAI API key not found in .env file")
set_openai_key(key)

flows = [
    greeter,
    [greeter, responder],
    [responder, summarizer],
    [summarizer, greeter],
    [greeter, router],
]

agency = Agency(
    flows,
    shared_instructions="",
    temperature=0.3,
)

#MAP Friendly routing tokens(strings) to the actual Agent object i created in my_agents.py
AGENT_MAP = {
    "GREETER": greeter,
    "RESPONDER": responder,
    "SUMMARIZER": summarizer,
}

VALID_KEYS = set(AGENT_MAP.keys())
# Builds a set of valid keys to make quick membership checks


def parse_router_output(text: str) -> str:

    # If the router returned nothing (empty string / None), default to GREETER
    if not text:
        return "GREETER"
    
    # Trim whitespace, split on whitespace, take the first token, and uppercase it.
    # This handles outputs like "GREETER", "greeter", or "GREETER please handle this".
    token = text.strip().split()[0].upper()
    if token in VALID_KEYS:
        return token
    
    
    # If the first word wasn't a valid token, try a more forgiving search:
    # convert the whole output to uppercase and see if any valid key appears anywhere inside.
    # This helps when the router returns "I think SUMMARIZER is best" or "choose: summarizer".

    up = text.upper()
    for k in VALID_KEYS:
        if k in up:
            return k
    
    # If no valid key was found, default to GREETER
    return "GREETER"


print("Swarm is running...Type 'exit' to stop.")
print("Prefix a message with '/sum ' to skip router and call summarizer directly.") # To help if summarizer is not working well
while True:
    user_msg = input("You: ")
    if user_msg.lower()== "exit" or user_msg.lower() == "quit":
        print("Exiting the swarm....")
        break

    if user_msg.lower().startswith("/sum "):
        payload = user_msg[len("/sum"):].strip()
        reply = agency.get_completion(payload, recipient_agent=summarizer)
        print("Summarizer:", reply)
        continue

    # Asking the Router agent to decide who should handle the message

    router_reply = agency.get_completion(user_msg, recipient_agent=router)
    # Turning the router's (possibly messy) textual reply into one of our canonical tokens
    router_token = parse_router_output(router_reply)

    # Map the token into the actual Agent object, defaulting to greeter if key not found
    selected_agent = AGENT_MAP.get(router_token, greeter)

    print(f"[Router decided] {router_token} -> forwarding to {selected_agent.name}")

    reply = agency.get_completion(user_msg, recipient_agent=selected_agent)
    print(f"{selected_agent.name}:", reply)






