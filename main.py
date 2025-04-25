from pathlib import Path

# Create directories if they don't exist
Path("data").mkdir(exist_ok=True)
Path("output").mkdir(exist_ok=True)
Path("tests/test_data").mkdir(parents=True, exist_ok=True)

from src.data_loader import load_data
from src.data_processor import clean_data, transform_data, save_to_sqlite
from src.analyzer import analyze_sales
from src.visualizer import plot_sales_by_category, plot_monthly_sales_trend
from pathlib import Path
import os

def ensure_data_dirs():
    """Ensure required directories exist"""
    Path("data").mkdir(exist_ok=True)
    Path("output").mkdir(exist_ok=True)

def main():
    ensure_data_dirs()
    
    # Load data
    data_path = Path("data/train.csv")
    if not data_path.exists():
        print(f"Error: Data file not found at {data_path}")
        return
    
    df = load_data(data_path)
    
    if df is not None:
        # Process data
        df = clean_data(df)
        df = transform_data(df)
        
        # Save to SQLite
        save_to_sqlite(df, "data/sales.db", "sales_data")
        
        # Analyze data
        analysis = analyze_sales(df)
        print("\nSales Analysis Summary:")
        print(f"Total Sales: ${analysis['total_sales']:,.2f}")
        print(f"Average Sale: ${analysis['avg_sale']:,.2f}")
        print(f"Maximum Sale: ${analysis['max_sale']:,.2f}")
        
        # Visualize data
        plot_sales_by_category(df)
        plot_monthly_sales_trend(df)

if __name__ == "__main__":
    main()