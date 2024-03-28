from agency_swarm.agents import Agent
from agency_swarm.tools import Retrieval
from agency_swarm.tools import CodeInterpreter


class CEOAgent(Agent):
    def __init__(self):
        super().__init__(
            name="CEOAgent",
            description="Directs the overall operation of the DataQualityAssuranceAgency, maintains communication with the DataQualityCheckPipeline Agent, and responds to reports from the AlertAgent.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[Retrieval, CodeInterpreter],
            tools_folder="./tools"
        )
