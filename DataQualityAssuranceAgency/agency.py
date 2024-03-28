from agency_swarm import Agency
from AlertAgent import AlertAgent
from DataQualityCheckPipelineAgent import DataQualityCheckPipelineAgent
from CEOAgent import CEOAgent
import os

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

ceo = CEOAgent()
dataQualityCheckPipeline = DataQualityCheckPipelineAgent()
alertAgent = AlertAgent()

agency = Agency([ceo, [ceo, dataQualityCheckPipeline],
                 [dataQualityCheckPipeline, alertAgent]],
                shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    completion_output = agency.get_completion("Perform the data quality checks between the 2 csv files and send any alert if discrepencies found", yield_messages=False)
    print(completion_output)
