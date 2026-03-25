import pandas as pd
from datetime import datetime

def generate_daily_dashboard(sales_data_path, output_path):
    """
    Automates the daily reporting workflow by processing raw sales data,
    cleaning anomalies, and exporting a formatted summary to Excel.
    """
    print("Initializing automated daily workflow...")
    
    # Load the raw daily data
    df = pd.read_csv(sales_data_path)
    
    # Clean data by removing incomplete transaction records
    cleaned_data = df.dropna(subset=['item_id', 'quantity_sold', 'transaction_time'])
    
    # Aggregate data to find peak sales hours
    cleaned_data['transaction_hour'] = pd.to_datetime(cleaned_data['transaction_time']).dt.hour
    peak_hours = cleaned_data.groupby('transaction_hour')['quantity_sold'].sum().reset_index()
    
    # Export the processed data directly to the dashboard file
    peak_hours.to_excel(output_path, sheet_name='Peak Hour Analysis', index=False)
    print(f"Workflow complete. Dashboard updated at {output_path}")

if __name__ == "__main__":
    # Example execution
    generate_daily_dashboard('raw_sales_log.csv', 'daily_management_dashboard.xlsx')