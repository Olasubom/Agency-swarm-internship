# Agency Swarm Internship - Day 2

## files
- my_agents.py -> greeter, responder, summarizer agents
- my_tools.py -> EchoTool, WordCountTool
- run_swarm.py -> starts the agency-swarm (v0.x)
- day2_outputs.txt -> outputs for three test messages

## errors faced and fixes

i keep getting an error the agents is not calling the WordCountTool i suspect the it s the flow causing this error 

### example of error
Swarm is running...Type 'exit' to stop.
You: hello world
Swarm: You said: hello world
You: 
###
As you can see am not getting a responce from the Summarize agent i tried fixing this by i tried to put Summarize agent as the recipient_agent but the greeter agent and the responder agent where longer sending a responce.

###

## Day2 fix 
i created a prompt to chack if the WordCountTool was been called and the tool is correct and the problem is the model not invoking it.
Here is the output ##

[Summarizer] running with: hello world
WordCountTool local test -> 2
EchoTool local test -> You said: hello world

so i tried Temporarily modify my runner so you can directly call summarizer for testing without re-wiring flows.
 ## code 
  if user_message.startswith("/sum "):
        # test the summarizer directly
        payload = user_message[len("/sum "):].strip()
        reply = agency.get_completion(payload, recipient_agent=summarizer)
        print("Summarizer:", reply)
        continue
### OUTPUT
Swarm is running...Type 'exit' to stop.
Prefix a message with '/sum ' to directly test the Summarizer (bypasses greeter).
You: /sum Hello world
[Summarizer] running with: Hello world
Summarizer: "Hello world" is a common greeting. (Word count: 2)
You: exit
Exiting the swarm.

### Why it happened 
The WordCountTool works and summarizer works when called directly.
But when i start the swarm at greeter the final printed reply was still Greeter’s echo. 
That’s a routing/hand-off issue: either the chain doesn’t end with summarizer, or your runner prints the first agent’s reply instead of the final agent’s reply.

#### Final fix 
Added a small conditional in run_swarm.py to forward the original user message to summarizer when the user asks for a summary
## CODE
 if "summarize" in user_message.lower() or user_message.lower().startswith("/sum"):
        reply = agency.get_completion(user_message, recipient_agent=summarizer)
        print("Summarizer:", reply)
        continue