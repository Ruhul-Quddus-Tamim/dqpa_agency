from agency_swarm.tools import BaseTool
from pydantic import Field
import pandas as pd

class UniquenessDuplicatesCheckTool(BaseTool):
    """
    Identifies and optionally removes duplicates in a CSV file to ensure data uniqueness.
    """

    filepath: str = Field(
        ..., description="Path to the CSV file to check for and handle duplicates."
    )
    columns: list = Field(
        optional=True, description="List of column names to check for duplicates. If not provided, checks the entire DataFrame."
    )
    remove_duplicates: bool = Field(
        ..., description="Whether to remove found duplicates from the CSV file."
    )

    def run(self):
        df = pd.read_csv(self.filepath)
        if self.columns:
            duplicate_rows = df.duplicated(subset=self.columns, keep='first').sum()
            if self.remove_duplicates:
                df = df.drop_duplicates(subset=self.columns, keep='first')
        else:
            duplicate_rows = df.duplicated(keep='first').sum()
            if self.remove_duplicates:
                df = df.drop_duplicates(keep='first')
        action_taken = 'Duplicates removed' if self.remove_duplicates else 'Duplicates identified'
        return f"{action_taken}: {duplicate_rows}"
