"""Module for processing and transforming sales data."""
import logging
from typing import Tuple

import numpy as np
import pandas as pd

from .exceptions import DataProcessingError

logger = logging.getLogger(__name__)

def process_sales_data(raw_df: pd.DataFrame) -> Tuple[pd.DataFrame, dict]:
    """Process raw sales data into clean, analysis-ready format.

    Args:
        raw_df: Raw DataFrame from load_data()

    Returns:
        Tuple: (processed_df, summary_stats)
        where summary_stats is a dictionary of key metrics

    Raises:
        DataProcessingError: If processing fails
    """
    try:
        logger.info("Processing %d rows of sales data", len(raw_df))
        
        processed_df = raw_df.copy()
        processed_df = processed_df.dropna(subset=['sale_amount'])
        processed_df['sale_date'] = pd.to_datetime(processed_df['sale_date'])
        
        summary_stats = {
            'total_sales': np.sum(processed_df['sale_amount']),
            'avg_sale': np.mean(processed_df['sale_amount']),
            'max_sale': np.max(processed_df['sale_amount'])
        }
        
        logger.info("Processing complete. Found %d valid records", len(processed_df))
        return processed_df, summary_stats
        
    except KeyError as e:
        error_msg = f"Missing required column: {str(e)}"
        logger.error(error_msg)
        raise DataProcessingError(error_msg) from e
    except Exception as e:
        error_msg = f"Unexpected processing error: {str(e)}"
        logger.error(error_msg)
        raise DataProcessingError(error_msg) from e
