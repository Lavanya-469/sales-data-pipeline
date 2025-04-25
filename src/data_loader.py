import pandas as pd
from pathlib import Path
from src.logger import setup_logger
from src.exceptions import DataLoadingError, DataValidationError

logger = setup_logger(__name__)

def validate_data(df):
    """Validate the loaded DataFrame"""
    required_columns = ['Order ID', 'Order Date', 'Sales', 'Category']
    if not all(col in df.columns for col in required_columns):
        missing = [col for col in required_columns if col not in df.columns]
        raise DataValidationError(f"Missing required columns: {missing}")
    return True

def load_data(file_path):
    """Load data from file with validation"""
    try:
        logger.info(f"Loading data from {file_path}")
        
        # Handle different file types
        if str(file_path).endswith('.csv'):
            df = pd.read_csv(file_path, parse_dates=['Order Date', 'Ship Date'])
        elif str(file_path).endswith('.parquet'):
            df = pd.read_parquet(file_path)
        else:
            raise DataLoadingError("Unsupported file format")
        
        validate_data(df)
        logger.info(f"Successfully loaded {len(df)} records")
        return df
        
    except Exception as e:
        logger.error(f"Failed to load data: {str(e)}")
        raise DataLoadingError(f"Data loading failed: {str(e)}") from e