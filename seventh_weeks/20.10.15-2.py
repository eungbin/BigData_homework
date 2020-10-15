#_*_coding:utf-8 _*_

import pandas as pd
import glob, re

def SaveData(files, totalData):
    excel_writer = pd.ExcelWriter(files,engine='xlsxwriter')
    totalData.to_excel(excel_writer,index=False,sheet_name='2011sheet')
    excel_writer.save()

columnlist = [u'2011인구수',u'2012인구수',u'2014인구수']   #각 파일의 [65세 이상_계] 필드명 수정(여백)
columnlist2 = [u'2011_65',u'2012_65',u'2014_65']
columnlist3 = [u'2011_65rate',u'2012_65rate',u'2014_65rate']
excel_files = glob.glob('./seongnam*.xlsx')

index=0
for f in excel_files:
    df = pd.read_excel(f)
    df2 = pd.DataFrame({u'행정기관':df[u'행정기관'],u'인구수':df[u'인구수_계'], u'65세 이상_계':df[u'65세 이상_계']})
    df2.rename(columns={u'행정기관': u'행정기관', u'인구수': columnlist[index],u'65세 이상_계': columnlist2[index]}, inplace=True)
    df2[columnlist3[index]] = df2[columnlist2[index]]/df2[columnlist[index]]*100
    f_new = re.sub(".xlsx", "_m.xlsx", f)
    SaveData(f_new, df2)
    index+=1

