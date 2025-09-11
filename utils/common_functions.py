import pandas as pd

def save_to_formats(df, base_filename):
    
    ### Save a DataFrame to CSV format with a consistent name.
    ### Example: save_to_formats(df, "output/csv/hcpcs_2025")
    ### will create "output/csv/hcpcs_2025.csv"

    filename = f"{base_filename}.csv"
    df.to_csv(filename, index=False)
   