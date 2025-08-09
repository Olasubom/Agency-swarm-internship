from agency_swarm import Agent
from my_tools import EchoTool, WordCountTool


greeter = Agent(
    name="Greeter",
    description="Greet the user warmly then echo their text inline.",
    model="gpt-3.5-turbo",
    instructions=(
        "When you receive a user's message, return ONE final plain-text response that "
        "includes a short greeting and the user's text. Use the EchoTool if you want, "
        "but make sure the final assistant response looks exactly like:\n"
        "  Hello! You said: <original user text>\n"
        "Do NOT return JSON or separate staged outputs."
    ),
    tools=[EchoTool],
    temperature=0.2,
    examples=[{"role": "user", "content": "Test", "attachments": [], "metadata": {}},
              {"role": "assistant", "content": "Hello! You said:"}
    ],

)

responder = Agent(
    name="Responder",
    description="repeats the questions back in verbatim",
    model="gpt-3.5-turbo",
    instructions="Whenever you get any text, echo it exactly using EchoTool",
    tools=[EchoTool],
    temperature=0.0,
    examples=[{"role": "user", "content": "Test", "attachments": [], "metadata": {}},
              {"role": "assistant", "content": "You said: Test"}
    ],
    
)

summarizer = Agent(
    name="Summarizer",
    description="Produce a one-sentence summary and include word count using WordCountTool.",
    model="gpt-3.5-turbo",
    instructions=(
        "Do these steps and return ONE plain-text sentence:\n"
        "1) Use WordCountTool with parameter text=<the user's message> to compute N.\n"
        "2) Produce a single short summary sentence of the user's message.\n"
        "3) Append ' (Word count: N)' to that one sentence.\n"
        "Important: do NOT return JSON or separate outputs — the final assistant reply MUST be a single sentence "
        "that contains the number. Example: 'Short summary here. (Word count: 9)'."
        
    ),
    tools=[WordCountTool, EchoTool],
    temperature=0.2,
   
    examples=[{"role": "user", "content": "This is a long text that needs summarization.", "attachments": [], "metadata": {}},
              {"role": "assistant", "content": "Summary: This is a long text that needs summarization.(word count: 8)", "attachments": [], "metadata": {}}
    ],
   
)