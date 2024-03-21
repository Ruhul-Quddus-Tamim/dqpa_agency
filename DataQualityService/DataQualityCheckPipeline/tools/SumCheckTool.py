from agency_swarm.tools import BaseTool
from pydantic import Field
import pandas as pd

class SumCheckTool(BaseTool):
    """
    Verifies the sum of a specific column in a CSV file against an expected value.
    """

    filepath: str = Field(
        ..., description="Path to the CSV file to perform the sum check on."
    )
    column: str = Field(
        ..., description="Name of the column to calculate the sum for."
    )
    expected_sum: float = Field(
        ..., description="Expected sum value for the specified column."
    )

    def run(self):
        df = pd.read_csv(self.filepath)
        actual_sum = df[self.column].sum()
        difference = abs(actual_sum - self.expected_sum)
        status = 'Match' if difference == 0 else f'Difference: {difference}'
        return f"Sum check for '{self.column}' column: {status}"
