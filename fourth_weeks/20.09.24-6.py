import pandas as pd
import glob

excel_data_files = [u'./4weeks_data/담당자별_판매량_Andy사원.xlsx',
                       u'./4weeks_data/담당자별_판매량_Becky사원.xlsx',
                       u'./4weeks_data/담당자별_판매량_Chris사원.xlsx']

total_data = pd.DataFrame()
for f in excel_data_files:
    df = pd.read_excel(f)
    total_data = total_data.append(df, ignore_index=True)

print(total_data)

excel_file_name = u'./4weeks_data/담당자별_판매량_통합.xlsx'
excel_total_file_writer = pd.ExcelWriter(excel_file_name, engine='xlsxwriter')
total_data.to_excel(excel_total_file_writer, index=False, sheet_name=u'담당자별_판매량_통합')
excel_total_file_writer.save()

print(glob.glob(excel_file_name))