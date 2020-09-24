import pandas as pd
import glob, re

excel_data_files1 = glob.glob(u'./4weeks_data/담당자별_판매량_*사원.xlsx')
for f in excel_data_files1:
    df = pd.read_excel(f)
    if(df.loc[1, '담당자'] == 'A'):
        df['담당자'] = 'Andy'
    elif(df.loc[1, '담당자'] == 'B'):
        df['담당자'] = 'Becky'
    elif(df.loc[1, '담당자'] == 'C'):
        df['담당자'] = 'Chris'

    f_new = re.sub(".xlsx", "2.xlsx", f)
    print(f_new)
    new_excel_file = pd.ExcelWriter(f_new, engine='xlsxwriter')
    df.to_excel(new_excel_file, index=False)
    new_excel_file.save()
