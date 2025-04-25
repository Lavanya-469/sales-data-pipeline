import pandas as pd
from pathlib import Path

def load_data(file_path):
    """Load CSV data into a pandas DataFrame"""
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data with {len(df)} rows")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def save_parquet(df, output_path):
    """Save DataFrame as Parquet file"""
    try:
        df.to_parquet(output_path)
        print(f"Data saved to {output_path}")
    except Exception as e:
        print(f"Error saving Parquet: {e}")

if __name__ == "__main__":
    # Dynamically build the path based on the script's location
    data_path = Path(__file__).resolve().parent.parent / "data" / "train.csv"
    
    # Load the data
    df = load_data(data_path)
    
    if df is not None:
        # Save the data as a Parquet file
        save_parquet(df, "../data/sales_data.parquet")
