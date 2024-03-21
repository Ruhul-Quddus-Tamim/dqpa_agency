from agency_swarm.tools import BaseTool
from pydantic import Field
import pandas as pd

class StringCheckTool(BaseTool):
    """
    Verifies if specified columns in a CSV file contain only string data types. 
    If you encounter any issue regarding the data type adjustment, please do adjust the string data types' column before you perform the checking.
    Make sure you don't get stuck by anything if you encounter any issue, you need to proceed.
    """

    filepath: str = Field(
        ..., description="Path to the CSV file to perform the string check on."
    )
    columns: list = Field(
        ..., description="List of column names to check for string data type."
    )

    def run(self):
        """
        If you encounter any issue regarding the data type adjustment, please do adjust the string data types' column before you perform the checking.
        Make sure you don't get stuck by anything if you encounter any issue, you need to proceed.
        """

        df = pd.read_csv(self.filepath)
        results = {}
        for column in self.columns:
            results[column] = 'String' if df[column].dtype == 'object' else 'Not String'
        return results
