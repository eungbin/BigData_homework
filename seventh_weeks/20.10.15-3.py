#_*_coding:utf-8 _*_

import pandas as pd
import glob



def SaveData(files, totalData):
    excel_writer = pd.ExcelWriter(files,engine='xlsxwriter')
    totalData.to_excel(excel_writer,index=False,sheet_name='2011_2014popular')
    excel_writer.save()

lastFile = pd.read_excel('./seongnam201409_m.xlsx')
totalData = pd.DataFrame({u'행정기관':lastFile[u'행정기관']})

excel_files = glob.glob('./seongnam*_m.xlsx')

for f in excel_files:
    df = pd.read_excel(f)
    totalData = pd.merge(totalData, df, how="outer")

excel_file_name = './Integration_seongnam2011_2014.xlsx'
SaveData(excel_file_name, totalData)
