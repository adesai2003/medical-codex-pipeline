import polars as pl
import pandas as pd
import time

npi_file_path = 'input/npidata_pfile_20050523-20250907.csv'

## just load the first n rows
start_time_polars = time.time()
df_polars = pl.read_csv(npi_file_path) #, n_rows=1_000_000)
end_time_polars = time.time()
elapsed_time_polars = end_time_polars - start_time_polars
print(elapsed_time_polars)

##see the time it takes to load with pandas
start_time_pandas = time.time()
df_pandas = pd.read_csv(npi_file_path, nrows=1000000, low_memory=False)
end_time_pandas = time.time()
elapsed_time_pandas = end_time_pandas - start_time_pandas
print(elapsed_time_pandas)

###result: polars is about 3x faster than pandas for this file

### columns we want to keep: NPI, Provider Last Name (Legal Name)
df_polars_small = df_polars.select([
    'NPI', 
    'Provider Last Name (Legal Name)'
])

## add in a last_updated column
df_polars_small = df_polars_small.with_columns(
    pl.lit('2025-09-03').alias('last_updated')
)

## rename colummns: code, description, last_updated
df_polars_small = df_polars_small.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description',
    'last_updated': 'last_updated'
})


## save to parquet
df_polars_small.write_parquet('output/npi_small.parquet')

#turn parquet back into csv
df_from_parquet = pl.read_parquet('output/npi_small.parquet')
df_from_parquet.write_csv('output/npi_small_from_parquet.csv')