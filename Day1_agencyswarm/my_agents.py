from agency_swarm import Agent
from my_tools import EchoTool

greeter = Agent(
    name = "Greeter",
    description = "greet the user warmly",
    instructions=(
        "When you recive a message responde with 'Hello' "
        "and the use the EchoTool to repeat the text"
    ),
    tools=[EchoTool],
    temperature=0.2,
     # model omitted → falls back to default_model(gpt-3.5-turbo)
    examples=[
        {
            "role": "user",
            "content": "Test",
            "attachments": [],
            "metadata": {},
        },
        {
            "role": "assistant",
            "content": "Hello! You said: Test",
            "attachments": [],
            "metadata": {},
        },
    ],
)



responder = Agent(
    name = "Responder",
    description = "repeats the questions back in verbatim",
    instructions= "When ever you get any text echo it excatly using EchoTool",
    tools=[EchoTool],
    temperature=0.0,
    # model omitted → falls back to default_model(gpt-3.5-turbo)
    examples=[
        {
            "role": "user",
            "content": "Test",
            "attachments": [],
            "metadata": {},
        },
        {
            "role": "assistant",
            "content": "Hello! You said: Test",
            "attachments": [],
            "metadata": {},
        },
    ],
)


