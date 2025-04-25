import pandas as pd
from pathlib import Path

class DataLoadingError(Exception):
    """Custom exception for data loading failures"""
    pass

def load_data(input_path: Path):
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(input_path)
        return df
    except FileNotFoundError as e:
        raise DataLoadingError(f"Input file not found: {input_path}") from e
    except Exception as e:
        raise DataLoadingError(f"Error loading data: {e}") from e