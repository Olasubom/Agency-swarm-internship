from agency_swarm.tools import BaseTool
from pydantic import Field

class EchoTool(BaseTool):
    # A simple tool that repeats back the provided text.
    text: str = Field(
        ...,
        description="The text to echo back.",
    )    

    def run(self) -> str:
        print(f"[EchoTool.run] called with text={self.text!r}")
        return f"You said: {self.text}"

class WordCountTool(BaseTool):
    # A tool that counts the number of words in the provided text.
    text: str = Field(
        ...,
        description="Text to count words for"
    )

    def run(self) -> int:
        print(f"[WordCountTool.run] called with text={self.text!r}")
        return len(self.text.split())