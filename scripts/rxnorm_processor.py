import polars as pl
from pathlib import Path
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
# https://www.nlm.nih.gov/research/umls/rxnorm/docs/techdoc.html#s12_10

##import the RXNATOMARCHIVE.RRF file
file_path = Path('input/RXNATOMARCHIVE.RRF')

logging.info(f"Reading RxNorm data from {file_path}")

## define the column names based on the RxNorm documentation
columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

logging.info("Defined column names for RxNorm data")

## read in with polars
rxnorm = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

logging.info(f"Read {len(rxnorm)} rows of RxNorm data into Polars DataFrame")

## save as csv
output_dir = Path('output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'RXNATOMARCHIVE.csv'

logging.info(f"Saving RxNorm data to {output_path}")

## save to csv
rxnorm.write_csv(output_path)

logging.info(f"RxNorm data saved to {output_path}")

##create a new file path to read in the csv we just created
new_file_path = Path('output/RXNATOMARCHIVE.csv')
rxnorm_small= pl.read_csv(new_file_path)

logging.info(f"Re-read RxNorm data from {new_file_path}")

#### Check potential column names that we think we want to keep: 
rxnorm_small = rxnorm_small.select(['aui', 'str', 'archive_timestamp'])

logging.info("Selected relevant columns from RxNorm data")

# rename columns
rxnorm_small = rxnorm_small.rename({
    'aui': 'code',
    'str': 'description',
    'archive_timestamp': 'last_updated',
})

logging.info("Renamed columns in RxNorm data")

## save to csv and parquet
file_output_path = 'output/rxnorm_small.csv'

output_path = 'output/rxnorm_small.csv'
rxnorm_small.write_csv(output_path)
rxnorm_small.write_parquet('output/rxnorm_small.parquet')

logging.info(f"RxNorm processed data saved to {file_output_path} and output/rxnorm_small.parquet")

#turn parquet back into csv
rxnorm_from_parquet = pl.read_parquet('output/rxnorm_small.parquet')
rxnorm_from_parquet.write_csv('output/rxnorm_from_parquet.csv')

logging.info("Converted RxNorm parquet data to CSV at output/rxnorm_from_parquet.csv")