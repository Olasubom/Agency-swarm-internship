from agency_swarm.tools import BaseTool
from pydantic import Field
from agency_swarm import Agent

class EchoTool(BaseTool):
    # A simple tool that repeats back the provided text.
    text: str = Field(
        ...,
        description="The text to echo back.",
    )    

    def run(self) -> str:
        return f"You said: {self.text}"