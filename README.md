# medical-codex-pipeline
**HHA 507 HOMEWORK 1**

## Step by Step Guide

### HCPCS
step 1: Take your input dataset `input/HCPC2025_OCT_ANWEB.txt`

step 2: adjust the columns using the script provided

step 3: use the script 

`output_path = "input/HCPC2025_OCT_ANWEB.csv"`

`df.to_csv(output_path, index=False)`

in order to covert the txt file into a csv file

step 4: Clean the dataset and look at column headers to decide what to use for code, description and last updated

step 5: save the cleaned dataset as a csv file under output

step 6: commit to githib using
    
    git add .
    
    git commit -m 'message'
    
    git push

### ICD
**US**

step 1:Take your input dataset `input/icd10cm_order_2025.txt`

step 2: convert the txt file into a csv file using the script provided

step 3: Clean the dataset and look at column headers to decide what to use for code, description and last updated

step 4: save the cleaned dataset as a csv file under output

step 5: commit to githib using

    git add .
    
    git commit -m 'message'
    
    git push

**WHO**

step 1:Take your input dataset `input/icd102019syst_codes.txt`

step 2: convert the txt file into a csv file using the script provided

step 3: Clean the dataset and look at column headers to decide what to use for code, description and last updated

step 4: save the cleaned dataset as a csv file under output

step 5: commit to githib using
    
    git add .
    
    git commit -m 'message'
    
    git push

### LOINC
step 1: look at the LOINC.csv dataset to see the column names choose what columns are to be kept

step 2: Once Columns are chosen, rename given column names into code, description and last_updated

step 3: save to csv file using

`file_output_path = 'output/loinc_small.csv''`

`loinc_small.to_csv('output/loinc_small.csv')`

step 4: use 

`loinc_small.to_csv('output/loinc_small_noindex.csv', index=False)` 

to remove the index

step 5: commit to githib using
    
    git add .
    
    git commit -m 'message'
    
    git push

### NPI
step 1: Import the file 

`input/npidata_pfile_20050523-20250907.csv` 

as a file path

step 2: Using that file path, view the dataset using polars. its faster to use polars than pandas becauce of how massive the dataset is 

step 3: Choose the columns to keep in the data set. In this case, we chose NPI, Provider Last Name (Legal Name). We added the last_updated column after using a seperate function. 

step 4: save the dataset as a parquet file by using 

`df_polars = pl.read_csv(npi_file_path) #, n_rows=1_000_000)`

step 5: turn the parquet back into a csv file using 

`df_from_parquet = pl.read_parquet('output/npi_small.parquet')`

`df_from_parquet.write_csv('output/npi_small_from_parquet.csv')`

step 6: commit to githib using
    
    git add .
    
    git commit -m 'message'
    
    git push

### RXNORM
step 1: Import the file 

`input/RXNATOMARCHIVE.RRF` 

as a file path

step 2: Using that file path, view the dataset using polars. its faster to use polars than pandas becauce of how massive the dataset is 

step 3: Choose the columns to keep in the data set. In this case, we chose NPI, Provider Last Name (Legal Name). We added the last_updated column after using a seperate function. 

step 4: save the dataset as a parquet file by using 

`output_dir = Path('output')`

`output_dir.mkdir(exist_ok=True)`

`output_path = output_dir / 'RXNATOMARCHIVE.csv'`

step 5: choose and rename the columns and save from a parquet to csv using 

`rxnorm_from_parquet = pl.read_parquet('output/rxnorm_small.parquet')`

`rxnorm_from_parquet.write_csv('output/rxnorm_from_parquet.csv')`


step 6: commit to githib using
    
    git add .
    
    git commit -m 'message'
    
    git push

## SNOWMED
step 1: Import the file 

`input/sct2_Description_Full-en_US1000124_20250901.txt` 

as a file path

step 2: Using that file path, view the dataset using polars. its faster to use polars than pandas becauce of how massive the dataset is 

step 3: Choose the columns to keep in the data set. In this case, we chose NPI, Provider Last Name (Legal Name). We added the last_updated column after using a seperate function. 

step 4: save the dataset as a parquet file by using 

`output_dir = Path('output')`

`output_dir.mkdir(exist_ok=True)`

`output_path = output_dir / 'sct2_Description_Full.csv''`

step 5: save to csv

step 6: create dataframe from

`df_snowmed = pl.read_csv(new_file_path)`


step 7: choose and rename the columns and save from a parquet to csv using 

`df_from_parquet = pl.read_parquet('output/snowmed_small.parquet')`

`df_from_parquet.write_csv('output/snowmed_small_from_parquet.csv')`

step 6: commit to githib using
    
    git add .
    
    git commit -m 'message'
    
    git push


### OUTPUTS
## The files were too big to commit to github so I put them in my google drive and submitted my public google drive link below. 

[https://drive.google.com/drive/folders/1XrMS8uZqQA6xZPy62udnvAHk-ZkfSK0c?usp=sharing](https://drive.google.com/drive/folders/1XrMS8uZqQA6xZPy62udnvAHk-ZkfSK0c?usp=sharing)