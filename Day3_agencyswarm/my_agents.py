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
              {"role": "assistant", "content": "Hello! You said: "}
    ],
)

responder = Agent(
    name="Responder",
    description="Repeats the questions back in verbatim.",
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
    instructions=("Do these steps and return ONE plain-text sentence:\n"
        "1) Use WordCountTool with parameter text=<the user's message> to compute N.\n"
        "2) Produce a single short summary sentence of the user's message.\n"
        "3) Append ' (Word count: N)' to that one sentence.\n"
        "Important: do NOT return JSON or separate outputs — the final assistant reply MUST be a single sentence "
        "that contains the number. Example: 'Short summary here. (Word count: 9)'."
    ),

    tools=[WordCountTool, EchoTool],
    temperature=0.1,
    examples=[{"role": "user", "content": "This is a long text that needs summarization.", "attachments": [], "metadata": {}},
              {"role": "assistant", "content": "Summary: This is a long text that needs summarization. (Word count: 8)", "attachments": [], "metadata": {}}
    ],
)

router = Agent(
    name="Router",
    description=(
        "Decides which specialist agent should handle the user's message. "
        "Return EXACTLY one of: GREETER, RESPONDER, SUMMARIZER (case insentitive). "
        "Do not return any extra text or punctuation. If unsure return GREETER."
    ),
    model="gpt-3.5-turbo",
    tools=[],
    instructions=(
        "You are a routing assistant. inspect the user's message and return ONE token only \n"
        "- GREETER: for simple greetings, small talk, or casual hello messages.\n"
        "- RESPONDER: for direct echo/clarification tasks or when user asks to repeat/verbatim.\n"
        "- SUMMARIZER: for requests that explicitly ask to summarize, analyze, or compute word counts "
        "(words like 'summarize', 'summary', 'shorten', 'summarise').\n"
        "Return only the single word (GREETER, RESPONDER, or SUMMARIZER)."
    ),
    temperature=0.0,
    examples=[{"role": "user", "content": "Hello there", "attachments": [], "metadata": {}},
              {"role": "assistant", "content": "GREETER", "attachments": [], "metadata": {}},

              {"role": "user", "content": "Can you repeat: The sky is blue", "attachments": [], "metadata": {}},
              {"role": "assistant", "content": "RESPONDER", "attachments": [], "metadata": {}},

              {"role": "user", "content": "Summarize this paragraph for me", "attachments": [], "metadata": {}},
              {"role": "assistant", "content": "SUMMARIZER", "attachments": [], "metadata": {}},
    ],
)