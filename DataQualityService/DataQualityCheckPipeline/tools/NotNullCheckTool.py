from agency_swarm.tools import BaseTool
from pydantic import Field
import pandas as pd

class NotNullCheckTool(BaseTool):
    """
    Verifies that specified columns in a CSV file do not contain null values.
    """

    filepath: str = Field(
        ..., description="Path to the CSV file to perform the not null check on."
    )
    columns: list = Field(
        ..., description="List of column names to verify for the absence of null values."
    )

    def run(self):
        df = pd.read_csv(self.filepath)
        results = {}
        for column in self.columns:
            results[column] = 'No Nulls' if df[column].notnull().all() else 'Contains Nulls'
        return results
