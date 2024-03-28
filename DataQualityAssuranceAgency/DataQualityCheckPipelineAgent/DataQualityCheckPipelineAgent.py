from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class DataQualityCheckPipelineAgent(Agent):
    def __init__(self):
        super().__init__(
            name="DataQualityCheckPipelineAgent",
            description="Responsible for executing data quality checks between two CSV files based on specified metrics and communicates with the AlertAgent to trigger alerts if discrepancies are found. Utilizes data processing and analysis tools, such as `pandas` for Python.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
