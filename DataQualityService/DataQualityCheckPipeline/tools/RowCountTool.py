from agency_swarm.tools import BaseTool
from pydantic import Field
import pandas as pd

class RowCountTool(BaseTool):
    """
    Retrieves the total number of rows in a CSV file.
    """

    filepath: str = Field(
        ..., description="Path to the CSV file to perform the row count check on."
    )

    def run(self):
        df = pd.read_csv(self.filepath)
        row_count = df.shape[0]
        return f"Total number of rows: {row_count}"
