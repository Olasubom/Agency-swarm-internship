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
