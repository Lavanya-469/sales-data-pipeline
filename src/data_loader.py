"""Module for loading and validating sales data from CSV files."""
from pathlib import Path

import pandas as pd
from .exceptions import DataLoadingError

def load_data(file_path: Path) -> pd.DataFrame:
    """Load and validate sales data from a CSV file.

    Args:
        file_path: Path to the CSV file containing sales data

    Returns:
        pd.DataFrame: Clean DataFrame containing sales data

    Raises:
        DataLoadingError: If file is missing, empty, or contains invalid data
    """
    try:
        df = pd.read_csv(file_path)
        
        if df.empty:
            raise DataLoadingError("File is empty")
        if 'sale_amount' not in df.columns:
            raise DataLoadingError("Missing required column: sale_amount")
            
        return df
        
    except FileNotFoundError as e:
        raise DataLoadingError(f"File not found: {file_path}") from e
    except pd.errors.EmptyDataError as e:
        raise DataLoadingError(f"Empty file: {file_path}") from e
    except pd.errors.ParserError as e:
        raise DataLoadingError(f"Invalid CSV format: {file_path}") from e
