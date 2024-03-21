from agency_swarm.agents import Agent
from agency_swarm.tools import Retrieval
from agency_swarm.tools import CodeInterpreter


class CEO(Agent):
    def __init__(self):
        super().__init__(
            name="CEO",
            description="This agent manages and coordinates tasks between the Data Quality Check Pipeline and the Report Generator agents, ensuring the workflow's efficiency and overseeing the entire data quality inspection process for the DataQualityInspector agency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter, Retrieval],
            tools_folder="./tools"
        )
