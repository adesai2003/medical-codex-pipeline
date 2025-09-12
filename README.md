# medical-codex-pipeline
**HHA 507 HOMEWORK 1**

## Step by Step Guide

### HCPCS
step 1: Take your input dataset `HHA-507-2025/Module1_MedicalCodexes/hcpcs/HCPC2025_OCT_ANWEB.txt`

step 2: adjust the columns using the script provided

step 3: use the script 

`output_path = "Module1_MedicalCodexes/hcpcs/output/HCPC2025_OCT_ANWEB.csv"`

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

step 1:Take your input dataset `HHA-507-2025/Module1_MedicalCodexes/icd/icd10cm_order_2025.txt`

step 2: convert the txt file into a csv file using the script provided

step 3: Clean the dataset and look at column headers to decide what to use for code, description and last updated

step 4: save the cleaned dataset as a csv file under output

step 5: commit to githib using

    git add .
    
    git commit -m 'message'
    
    git push

**WHO**

step 1:Take your input dataset `HHA-507-2025/Module1_MedicalCodexes/icd/who/icd102019syst_codes.txt`

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

`file_output_path = 'HHA-507-2025/Module1_MedicalCodexes/loinc/output/loinc_small.csv'`

`loinc_small.to_csv('HHA-507-2025/Module1_MedicalCodexes/loinc/output/loinc_small.csv')`

step 4: use 

`loinc_small.to_csv('HHA-507-2025/Module1_MedicalCodexes/loinc/output/loinc_small_noindex.csv', index=False` 

to remove the index

step 5: commit to githib using
    
    git add .
    
    git commit -m 'message'
    
    git push

### NPI
step 1: Import the file 

`HHA-507-2025/Module1_MedicalCodexes/npi/npidata_pfile_20050523-20250810.csv` 

as a file path

step 2: Using that file path, view the dataset using polars. its faster to use polars than pandas becauce of how massive the dataset is 

step 3: Choose the columns to keep in the data set. In this case, we chose NPI, Provider Last Name (Legal Name). We added the last_updated column after using a seperate function. 

step 4: save the dataset as a parquet file by using 

`df_polars_small.write_parquet('HHA-507-2025/Module1_MedicalCodexes/npi/output/npi_small.parquet)`

step 5: turn the parquet back into a csv file using 

`df_from_parquet = pl.read_parquet('HHA-507-2025/Module1_MedicalCodexes/npi/output/npi_small.parquet'`

`df_from_parquet.write_csv('HHA-507-2025/Module1_MedicalCodexes/npi/output/npi_small_from_parquet.csv')`

step 6: commit to githib using
    
    git add .
    
    git commit -m 'message'
    
    git push

### RXNORM
kajklj;aj;jsa;;sljkfjalkjflkjsajkfjlkasljf