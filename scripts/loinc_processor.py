import pandas as pd 
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

## Input/Loinc.csv
loinc = pd.read_csv('input/Loinc.csv')

logging.info("Loinc.csv file read into DataFrame")

### Info to describe 
loinc.info()

logging.info("Displayed DataFrame info")

### Strings 
loinc.STATUS.value_counts()

logging.info("Displayed value counts for STATUS column")

### print first row
loinc.iloc[0]
logging.info("Displayed first row of LOINC DataFrame")

#### Check potential column names that we think we want to keep: LOINC_NUM, DefinitionDescription
loinc.LOINC_NUM
loinc.LONG_COMMON_NAME

logging.info("Selected relevant columns from LOINC data")

#create a smaller dataframe with just the columns we want
list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME']

logging.info("Created list of columns to keep")

### create the smaller dataframe
loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]
loinc_small = loinc[list_cols]

logging.info("Created smaller DataFrame with selected columns")

##add in a last_updated column
loinc_small['last_updated'] = '2025-09-03'

logging.info("Added last_updated column to LOINC data")

# loinc_small = loinc_small.rename(columns={})
loinc_small = loinc_small.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'description',
})

logging.info("Renamed columns in LOINC data")

#save to csv
file_output_path = 'output/loinc_small.csv'

logging.info(f"Saving processed LOINC data to {file_output_path}")

##convert to csv
loinc_small.to_csv('output/loinc_small.csv')

logging.info(f"LOINC processed data saved to {file_output_path}")

##save to csv without index
loinc_small.to_csv('output/loinc_small_noindex.csv', index=False)

logging.info(f"LOINC processed data saved to output/loinc_small_noindex.csv without index")