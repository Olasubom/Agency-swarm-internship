from agency_swarm import Agent
from my_tools import EchoTool, WordCountTool


greeter = Agent(
    name="Greeter",
    description="greet the user warmly",
    instructions=(
        "When you receive a message, respond with 'Hello' "
        "and use the EchoTool to repeat the text"
    ),
    tools=[EchoTool],
    temperature=0.2,
    model="gpt-3.5-turbo",
    examples=[{"role": "user", "content": "Test", "attachments": [], "metadata": {}},
              {"role": "assistant", "content": "Hello! You said:"}
    ],

)

responder = Agent(
    name="Responder",
    description="repeats the questions back in verbatim",
    instructions="Whenever you get any text, echo it exactly using EchoTool",
    tools=[EchoTool],
    temperature=0.0,
    model="gpt-3.5-turbo",
    examples=[{"role": "user", "content": "Test", "attachments": [], "metadata": {}},
              {"role": "assistant", "content": "You said: Test"}
    ],
)

summarizer = Agent(
    name="Summarizer",
    description="Produce a one-sentence summary of the user's text and report word count.",
    instructions=(
        "1) Read the user's message.\n"
        "2) Use WordCountTool to compute the number of words in the user's message.\n"
        "3) Produce a single-sentence summary (one short sentence) of the message.\n"
        "4) Output the summary followed by ' (Word count: N)'.\n"
        "If useful, you may also use EchoTool to validate the input before summarizing."
        
    ),
    tools=[WordCountTool, EchoTool],
    temperature=0.2,
    model="gpt-3.5-turbo",
    examples=[{"role": "user", "content": "This is a long text that needs summarization.", "attachments": [], "metadata": {}},
              {"role": "assistant", "content": "Summary: This is a long text that needs summarization.(word count: 8)", "attachments": [], "metadata": {}}
    ],
)