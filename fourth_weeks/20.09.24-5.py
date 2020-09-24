import pandas as pd

df = pd.read_excel(u'./4weeks_data/학생시험성적.xlsx', sheet_name=u'2차시험', index_col=u'학생')
print(df)

excel_exam_data1 = {u'학생': ['A', 'B', 'C', 'D', 'E', 'F'],
                        u'국어': [80, 90, 95, 70, 75, 85],
                        u'영어': [90, 95, 70, 85, 90, 95],
                        u'수학': [85, 95, 75, 80, 85, 100]}
df1 = pd.DataFrame(excel_exam_data1, columns=[u'학생', u'국어', u'영어', u'수학'])

excel_exam_data2 = {u'학생': ['A', 'B', 'C', 'D', 'E', 'F'],
                    u'국어' : [85, 95, 75, 80, 85, 100],
                    u'영어': [80, 90, 95, 70, 75, 85],
                    u'수학': [90, 95, 70, 85, 90, 95]}
df2 = pd.DataFrame(excel_exam_data2, columns=[u'학생', u'국어', u'영어', u'수학'])

excel_writer2 = pd.ExcelWriter(u'./학생시험성적_수정.xlsx', engine='xlsxwriter')
df1.to_excel(excel_writer2, index=False, sheet_name=u'중간고사')
df2.to_excel(excel_writer2, index=False, sheet_name=u'기말고사')
excel_writer2.save()