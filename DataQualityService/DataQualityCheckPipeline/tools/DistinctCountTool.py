from agency_swarm.tools import BaseTool
from pydantic import Field
import pandas as pd

class DistinctCountTool(BaseTool):
    """
    Counts distinct observations over requested axis in a CSV file.
    """

    filepath: str = Field(
        ..., description="Path to the CSV file to perform the distinct count check on."
    )
    column: str = Field(
        ..., description="Name of the column to calculate the distinct count for."
    )

    def run(self):
        df = pd.read_csv(self.filepath)
        distinct_count = df[self.column].nunique()
        return f"Distinct count in '{self.column}' column: {distinct_count}"
