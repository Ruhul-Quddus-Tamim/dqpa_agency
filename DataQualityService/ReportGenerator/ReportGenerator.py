from agency_swarm.agents import Agent
from agency_swarm.tools import Retrieval
from agency_swarm.tools import CodeInterpreter

class ReportGenerator(Agent):
    def __init__(self):
        super().__init__(
            name="ReportGenerator",
            description="This agent is tasked with generating a comprehensive report in document format after receiving a successful status code from the Data Quality Check Pipeline agent for the DataQualityInspector agency. The report summarizes the results of the data quality checks and includes suggestions for data quality improvements.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter, Retrieval],
            tools_folder="./tools"
        )
