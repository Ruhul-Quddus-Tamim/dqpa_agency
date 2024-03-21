from agency_swarm.agents import Agent
from agency_swarm.tools import Retrieval
from agency_swarm.tools import CodeInterpreter


class DataQualityCheckPipeline(Agent):
    def __init__(self):
        super().__init__(
            name="DataQualityCheckPipeline",
            description="This agent performs data quality checks on CSV files, including Distinct Count, Row Count, String Check, Sum Check, Not Null Check, and Uniqueness/Duplicates for the DataQualityInspector agency. It iteratively solves any encountered issues until a successful status code of 200 is achieved, indicating all data quality checks have passed without error.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter, Retrieval],
            tools_folder="./tools"
        )
