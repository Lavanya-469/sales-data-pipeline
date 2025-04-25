import pandas as pd
import numpy as np
from src.logger import setup_logger
from src.exceptions import TransformationError

logger = setup_logger(__name__)

def add_advanced_features(df):
    """Add derived features to the data"""
    try:
        logger.info("Adding advanced features")
        
        # Date features
        df['Order_Year'] = df['Order Date'].dt.year
        df['Order_Month'] = df['Order Date'].dt.month
        df['Day_of_Week'] = df['Order Date'].dt.day_name()
        
        # Business features
        df['Processing_Time'] = (df['Ship Date'] - df['Order Date']).dt.days
        df['High_Value'] = df['Sales'] > df['Sales'].quantile(0.9)
        
        logger.info("Successfully added advanced features")
        return df
        
    except Exception as e:
        logger.error(f"Feature engineering failed: {str(e)}")
        raise TransformationError(f"Feature engineering failed: {str(e)}") from e