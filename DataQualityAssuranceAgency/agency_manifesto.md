# DataQualityAssuranceAgency Manifesto

### Mission:
The mission of the DataQualityAssuranceAgency is to ensure the highest standards of data quality by performing comprehensive data quality checks between two CSV files. The agency will focus on distinct count, row count, string check, sum check, not null check, schema check, and uniqueness/duplicates. It will maintain a seamless communication flow to address any data quality issues promptly.

### Agency Structure:
1. **CEO Agent**: This agent directs the overall operation of the agency. It initiates and maintains communication with the DataQualityCheckPipeline Agent throughout the data quality checking process and acts upon the reports received from the AlertAgent if discrepancies are found.

2. **DataQualityCheckPipeline Agent**: This agent is the core of the agency, responsible for executing data quality checks between two CSV files based on the specified metrics. If discrepancies are detected, it communicates with the AlertAgent to trigger an alert.

3. **AlertAgent**: This agent is tasked with sending alerts via email through Gmail SMTP server. It activates upon receiving a discrepancy report from the DataQualityCheckPipeline Agent, detailing the type(s) of data quality check mismatch.

The CSV files will be stored in the `files` folder for access by the `DataQualityCheckPipelineAgent` agent.