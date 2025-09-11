import pandas as pd

# Path to the HCPCS text file
file_path = "Module1_MedicalCodexes/hcpcs/HCPC2025_OCT_ANWEB.txt"

# Read the file into a DataFrame
# The file appears to be fixed-width formatted, so we'll use read_fwf

# You may need to adjust colspecs based on actual column widths
# Here is a simple guess based on the sample
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]
df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)


## save as csv to Module1_MedicalCodexes/hcpcs/output
output_path = "Module1_MedicalCodexes/hcpcs/output/HCPC2025_OCT_ANWEB.csv"
df.to_csv(output_path, index=False)

#print first row
df.iloc[0]

#### Check potential column names that we think we want to keep: Code, Description1
df.Code
df.Description1

df_hcpcs = df[['Code', 'Description1']]

##add in a last_updated column
df_hcpcs['last_updated'] = '2025-09-03'

df_hcpcs = df_hcpcs.rename(columns={
    'Code': 'code',
    'Description1': 'description',
})

file_output_path = 'HHA-507-2025/Module1_MedicalCodexes/hcpcs/output/hcpcs_small.csv'
df_hcpcs.to_csv('HHA-507-2025/Module1_MedicalCodexes/hcpcs/output/hcpcs_small.csv')
df_hcpcs.to_csv('HHA-507-2025/Module1_MedicalCodexes/hcpcs/output/hcpcs_small_noindex.csv', index=False)