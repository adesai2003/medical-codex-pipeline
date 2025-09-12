import pandas as pd
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
## Set up logging
logging.info("Starting HCPCS processing script")

# Path to the HCPCS text file
file_path = "input/HCPC2025_OCT_ANWEB.txt"

logging.info(f"Reading HCPCS data from {file_path}")


# Read the file into a DataFrame

# The file appears to be fixed-width formatted, so we'll use read_fwf

# You may need to adjust colspecs based on actual column widths
# Here is a simple guess based on the sample
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]
df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)

logging.info("HCPCS data read into DataFrame")

## save as csv 
output_path = "input/HCPC2025_OCT_ANWEB.csv"
df.to_csv(output_path, index=False)

logging.info(f"HCPCS data saved to {output_path}")

#print first row
df.iloc[0]

#### Check potential column names that we think we want to keep: Code, Description1
df.Code
df.Description1

df_hcpcs = df[['Code', 'Description1']]

logging.info("Selected relevant columns from HCPCS data")

##add in a last_updated column
df_hcpcs['last_updated'] = '2025-09-03'

##rename columns
df_hcpcs = df_hcpcs.rename(columns={
    'Code': 'code',
    'Description1': 'description',
})

logging.info("Renamed columns and added last_updated column")

#save to csv
file_output_path = 'output/hcpcs_full.csv'
df_hcpcs.to_csv('output/hcpcs_full.csv')
df_hcpcs.to_csv('output/hcpcs_full_noindec.csv', index=False)

logging.info(f"HCPCS processed data saved to {file_output_path}")