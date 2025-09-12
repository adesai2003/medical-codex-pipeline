import pandas as pd
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

#define the file path
file_path = 'input/icd102019syst_codes.txt'

logging.info(f"Reading ICD-10-WHO data from {file_path}")

### columns in the file
columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

#read in the file
icdcodeswho = pd.read_csv(file_path, sep=';', header=None, names=columns)

logging.info(f"Read {len(icdcodeswho)} rows of ICD-10-WHO data")

## save as csv
output_path = 'output/icd10who_full.csv'
icdcodeswho.to_csv(output_path, index=False)

logging.info(f"ICD-10-WHO data saved to {output_path}")

### print first row
icdcodeswho.iloc[0]

logging.info("Displayed first row of ICD-10-WHO DataFrame")

#colums we want to keep: code, titele_en
icdcodeswho.code
icdcodeswho.title_en

logging.info("Selected relevant columns from ICD-10-WHO data")

#create a smaller dataframe with just the columns we want
icdcodeswho_small = icdcodeswho[['code', 'title_en']]

logging.info("Created smaller DataFrame with selected columns")


##add in a last_updated column
icdcodeswho_small['last_updated'] = '2025-01-03'

logging.info("Added last_updated column to ICD-10-WHO data")

##rename columns
icdcodeswho_small = icdcodeswho_small.rename(columns={
    'code': 'code',
    'title_en': 'description',
})      

logging.info("Renamed columns in ICD-10-WHO data")

#save to csv
file_output_path = 'output/icd10who_small.csv'
icdcodeswho_small.to_csv(file_output_path, index=False)
icdcodeswho_small.to_csv('output/icd10who_small_noindex.csv', index=False)

logging.info(f"ICD-10-WHO processed data saved to {file_output_path}")