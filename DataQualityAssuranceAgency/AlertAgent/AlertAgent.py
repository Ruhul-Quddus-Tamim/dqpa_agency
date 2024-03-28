from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class AlertAgent(Agent):
    def __init__(self):
        super().__init__(
            name="AlertAgent",
            description="Responsible for sending alerts via email through Gmail SMTP server when discrepancies are reported by the DataQualityCheckPipeline Agent. Should have access to an SMTP client or API to send out alerts",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
