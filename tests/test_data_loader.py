from pathlib import Path
import pytest
from src.data_loader import load_data, DataLoadingError

def test_load_data_success():
    """Test loading data from a valid CSV file"""
    test_file = Path(__file__).parent / "test_data/sample_sales.csv"  # Correct path
    df = load_data(test_file)
    assert not df.empty  # Check the loaded data is valid

def test_load_data_failure():
    """Test handling of non-existent file"""
    with pytest.raises(DataLoadingError):  # Expect custom exception
        load_data(Path("nonexistent_file.csv"))