import polars as pl
from pathlib import Path

# https://www.nlm.nih.gov/research/umls/rxnorm/docs/techdoc.html#s12_10

file_path = Path('input/RXNATOMARCHIVE.RRF')

columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

rxnorm = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

output_dir = Path('output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'RXNATOMARCHIVE.csv'

rxnorm.write_csv(output_path)

new_file_path = Path('output/RXNATOMARCHIVE.csv')
rxnorm_small= pl.read_csv(new_file_path)

#### Check potential column names that we think we want to keep: 
rxnorm_small = rxnorm_small.select(['aui', 'str', 'archive_timestamp'])

# rename columns
rxnorm_small = rxnorm_small.rename({
    'aui': 'code',
    'str': 'description',
    'archive_timestamp': 'last_updated',
})

file_output_path = 'output/rxnorm_small.csv'

output_path = 'output/rxnorm_small.csv'
rxnorm_small.write_csv(output_path)
rxnorm_small.write_parquet('output/rxnorm_small.parquet')

#turn parquet back into csv
rxnorm_from_parquet = pl.read_parquet('output/rxnorm_small.parquet')
rxnorm_from_parquet.write_csv('output/rxnorm_from_parquet.csv')
