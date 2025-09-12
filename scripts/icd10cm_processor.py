import pandas as pd 
import re
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
# Define the file path
file_path= 'input/icd10cm_order_2025.txt'

logging.info(f"Reading ICD-10-CM data from {file_path}")

# This initializes a blank list to hold the parsed codes (one dict per line)
codes = []

with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
    for i, line in enumerate(file, 1):
        # Keep the newline out, keep spaces (they matter for fixed width)
        line = line.rstrip("\r\n")

        # Skip empty/very short lines
        if not line.strip() or len(line) < 16:
            continue

        # ---- Fixed-width slices (0-based, end-exclusive) ----
        # First 6 characters (positions 0..5)
        order_num = line[0:6].strip()

        # Characters 7..13  (0-based 6..12)
        code = line[6:13].strip()

        # Character 15 (0-based 14)
        level = line[14:15].strip()

        # Everything after position 16 (0-based) is text
        remaining_text = line[16:]

        # Split description vs detailed description by 4+ spaces
        parts = re.split(r"\s{4,}", remaining_text, maxsplit=1)
        description = parts[0].strip() if len(parts) > 0 else ""
        description_detailed = parts[1].strip() if len(parts) > 1 else ""

        # Only keep rows that actually have a code
        if code:
            codes.append({
                "order_num": order_num,
                "code": code,
                "level": level,
                "description": description,
                "description_detailed": description_detailed
            })

logging.info(f"Parsed {len(codes)} ICD-10-CM codes from the file")

## Create a DataFrame from the parsed codes
icdcodes = pd.DataFrame(codes)

logging.info("Created DataFrame from parsed ICD-10-CM codes")

## Save the DataFrame to a CSV file
file_path_new= "output/icd10cm_order_2025.csv"
icdcodes.to_csv(file_path_new)

logging.info("Saved full ICD-10-CM data to output/icd10cm_order_2025.csv")

# Read the file into a DataFrame
icdcodes =pd.read_csv(file_path_new)

logging.info("ICD-10-CM data read into DataFrame")

#print first row
icdcodes.iloc[0]
logging.info("Displayed first row of ICD-10-CM DataFrame")

#### Check potential column names that we think we want to keep: code, description_detailed
icdcodes.code
icdcodes.description_detailed

icdcodes = icdcodes[['code', 'description_detailed']]

logging.info("Selected relevant columns from ICD-10-CM data")

##add in a last_updated column
icdcodes['last_updated'] = '2025-11-03'

logging.info("Added last_updated column to ICD-10-CM data")

##rename columns
icdcodes = icdcodes.rename(columns={
    'Code': 'code',
    'Description1': 'description',
})

logging.info("Renamed columns in ICD-10-CM data")

#save to csv
icdcodes.to_csv("output/icd10cm_order_2025_processed.csv")
icdcodes.to_csv("output/icd10cm_order_2025_noindex.csv", index=False)

logging.info("Saved processed ICD-10-CM data to output/icd10cm_order_2025_processed.csv and output/icd10cm_order_2025_noindex.csv")

