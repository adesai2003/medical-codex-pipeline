import polars as pl
from pathlib import Path

file_path = Path('HHA-507-2025/Module1_MedicalCodexes/snowmed/sct2_Description_Full-en_US1000124_20250901.txt')

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

output_dir = Path('HHA-507-2025/Module1_MedicalCodexes/snowmed/output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'sct2_Description_Full.csv'

df_snowmed.write_csv(output_path)

##create a new file path to read in the csv we just created
new_file_path = Path('HHA-507-2025/Module1_MedicalCodexes/snowmed/output/sct2_Description_Full.csv')

### create dataframe from csv
df_snowmed = pl.read_csv(new_file_path)


### select only the columns we want to keep: id, term
df_snowmed = df_snowmed.select([
    'id', 
    'term'
])

## add in a last_updated column
df_snowmed = df_snowmed.with_columns(
    pl.lit('2025-06-03').alias('last_updated')
)

## rename colummns: code, description, last_updated
df_snowmed = df_snowmed.rename({
    'id': 'code',
    'term': 'description',
})


## save to parquet
df_snowmed.write_parquet('HHA-507-2025/Module1_MedicalCodexes/snowmed/output/snowmed_small.parquet')

#turn parquet back into csv
df_from_parquet = pl.read_parquet('HHA-507-2025/Module1_MedicalCodexes/snowmed/output/snowmed_small.parquet')
df_from_parquet.write_csv('HHA-507-2025/Module1_MedicalCodexes/snowmed/output/snowmed_small_from_parquet.csv')