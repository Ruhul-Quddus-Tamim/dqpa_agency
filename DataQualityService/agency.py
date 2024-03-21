from agency_swarm import Agency
from ReportGenerator import ReportGenerator
from DataQualityCheckPipeline import DataQualityCheckPipeline
from CEO import CEO
import os

os.environ["OPENAI_API_KEY"] = ""

ceo = CEO()
dataQualityCheckPipeline = DataQualityCheckPipeline()
reportGenerator = ReportGenerator()

agency = Agency([
    ceo,
    [ceo, dataQualityCheckPipeline],
    [ceo, reportGenerator],
    [dataQualityCheckPipeline, reportGenerator]
],
shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    completion_output = agency.get_completion("Perform the data quality checks and generate the report", yield_messages=False)
    print(completion_output)