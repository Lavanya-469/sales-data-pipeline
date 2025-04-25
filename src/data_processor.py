import pandas as pd
from sqlalchemy import create_engine

def clean_data(df):
    """Clean and preprocess the data"""
    # Convert date columns to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')
    
    # Handle missing values
    df.fillna({'Postal Code': 'Unknown'}, inplace=True)
    
    return df

def transform_data(df):
    """Transform data by adding derived columns"""
    # Calculate days to ship
    df['Days to Ship'] = (df['Ship Date'] - df['Order Date']).dt.days
    
    # Extract year and month from order date
    df['Order Year'] = df['Order Date'].dt.year
    df['Order Month'] = df['Order Date'].dt.month_name()
    
    return df

def save_to_sqlite(df, db_path, table_name):
    """Save data to SQLite database"""
    try:
        engine = create_engine(f'sqlite:///{db_path}')
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data saved to SQLite database at {db_path}")
    except Exception as e:
        print(f"Error saving to SQLite: {e}")

if __name__ == "__main__":
    # Example usage
    from data_loader import load_data
    data_path = Path("../data/train.csv")
    df = load_data(data_path)
    if df is not None:
        df = clean_data(df)
        df = transform_data(df)
        save_to_sqlite(df, "../data/sales.db", "sales_data")