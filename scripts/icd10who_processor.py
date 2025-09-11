import pandas as pd

file_path = 'HHA-507-2025/Module1_MedicalCodexes/icd/who/icd102019syst_codes.txt'

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

icdcodeswho = pd.read_csv(file_path, sep=';', header=None, names=columns)

output_path = 'HHA-507-2025/Module1_MedicalCodexes/icd/who/output/icd10who.csv'
icdcodeswho.to_csv(output_path, index=False)


### print first row
icdcodeswho.iloc[0]

#colums we want to keep: code, titele_en
icdcodeswho.code
icdcodeswho.title_en

icdcodeswho_small = icdcodeswho[['code', 'title_en']]

##add in a last_updated column
icdcodeswho_small['last_updated'] = '2025-01-03'

icdcodeswho_small = icdcodeswho_small.rename(columns={
    'code': 'code',
    'title_en': 'description',
})      

#save to csv
file_output_path = 'HHA-507-2025/Module1_MedicalCodexes/icd/who/output/icd10who_small.csv'
icdcodeswho_small.to_csv(file_output_path, index=False)
icdcodeswho_small.to_csv('HHA-507-2025/Module1_MedicalCodexes/icd/who/output/icd10who_small_noindex.csv', index=False)