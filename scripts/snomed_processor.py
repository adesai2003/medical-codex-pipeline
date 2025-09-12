import polars as pl
from pathlib import Path
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

## describe file path
file_path = Path('input/sct2_Description_Full-en_US1000124_20250901.txt')

logging.info(f"Reading SNOMED CT data from {file_path}")

## read in with polars
df_snowmed = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)

logging.info(f"Read {len(df_snowmed)} rows of SNOMED CT data into Polars DataFrame")

## save as csv
output_dir = Path('output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'sct2_Description_Full.csv'

logging.info(f"Saving SNOMED CT data to {output_path}")

## save to csv
df_snowmed.write_csv(output_path)

logging.info(f"SNOMED CT data saved to {output_path}")

##create a new file path to read in the csv we just created
new_file_path = Path('output/sct2_Description_Full.csv')

logging.info(f"Re-reading SNOMED CT data from {new_file_path}")

### create dataframe from csv
df_snowmed = pl.read_csv(new_file_path)

logging.info(f"Re-read {len(df_snowmed)} rows of SNOMED CT data into Polars DataFrame")

### select only the columns we want to keep: id, term
df_snowmed = df_snowmed.select([
    'id', 
    'term'
])

logging.info("Selected relevant columns from SNOMED CT data")

## add in a last_updated column
df_snowmed = df_snowmed.with_columns(
    pl.lit('2025-06-03').alias('last_updated')
)

logging.info("Added last_updated column to SNOMED CT data")

## rename colummns: code, description, last_updated
df_snowmed = df_snowmed.rename({
    'id': 'code',
    'term': 'description',
})

logging.info("Renamed columns in SNOMED CT data")

## save to parquet
df_snowmed.write_parquet('output/snowmed_small.parquet')

logging.info("Saved processed SNOMED CT data to output/snowmed_small.parquet")

#turn parquet back into csv
df_from_parquet = pl.read_parquet('output/snowmed_small.parquet')
df_from_parquet.write_csv('output/snowmed_small_from_parquet.csv')

logging.info("Converted SNOMED CT parquet data to CSV at output/snowmed_small_from_parquet.csv")