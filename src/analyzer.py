import pandas as pd
import sqlalchemy as db

def analyze_sales(df):
    """Perform sales analysis"""
    analysis = {}
    
    # Basic statistics
    analysis['total_sales'] = df['Sales'].sum()
    analysis['avg_sale'] = df['Sales'].mean()
    analysis['max_sale'] = df['Sales'].max()
    
    # Sales by category
    analysis['sales_by_category'] = df.groupby('Category')['Sales'].sum().to_dict()
    
    # Top products
    analysis['top_products'] = (
        df.groupby('Product Name')['Sales']
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .to_dict()
    )
    
    return analysis

def analyze_from_sql(db_path, table_name):
    """Analyze data from SQL database"""
    try:
        engine = db.create_engine(f'sqlite:///{db_path}')
        connection = engine.connect()
        metadata = db.MetaData()
        sales_data = db.Table(table_name, metadata, autoload=True, autoload_with=engine)
        
        # Example query
        query = db.select([
            sales_data.columns.Category,
            db.func.sum(sales_data.columns.Sales).label('Total Sales')
        ]).group_by(sales_data.columns.Category)
        
        result = connection.execute(query).fetchall()
        return dict(result)
    except Exception as e:
        print(f"Error analyzing from SQL: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    from data_loader import load_data
    from data_processor import clean_data, transform_data
    
    data_path = Path("../data/train.csv")
    df = load_data(data_path)
    if df is not None:
        df = clean_data(df)
        df = transform_data(df)
        analysis = analyze_sales(df)
        print("Sales Analysis:")
        print(analysis)
        
        # SQL analysis example
        sql_analysis = analyze_from_sql("../data/sales.db", "sales_data")
        print("\nSQL Analysis:")
        print(sql_analysis)