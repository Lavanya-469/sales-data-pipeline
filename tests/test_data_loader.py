import pytest
from pathlib import Path
from src.data_loader import load_data

def test_load_data_success():
    """Test loading data from a valid CSV file"""
    test_file = Path("tests/test_data/sample_sales.csv")
    df = load_data(test_file)
    assert df is not None
    assert len(df) > 0

def test_load_data_failure():
    """Test handling of non-existent file"""
    df = load_data(Path("nonexistent_file.csv"))
    assert df is None