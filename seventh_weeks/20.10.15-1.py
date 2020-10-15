import pandas as pd

df = pd.read_excel('./sea_rain.xlsx', sheet_name='Sheet1')
excel_chart = pd.ExcelWriter('./sea_rain_1.xlsx', engine='xlsxwriter')
df.to_excel(excel_chart, index=False, sheet_name='Sheet1')
workbook = excel_chart.book
worksheet = excel_chart.sheets['Sheet1']

chart = workbook.add_chart({'type': 'line'})
chart.add_series({'values': '=Sheet1!$B$2:$B$6', 'categories':'=Sheet1!$A$2:$A$6','name':'=Sheet1!$B$1'})
chart.add_series({'values': '=Sheet1!$C$2:$C$6', 'categories':'=Sheet1!$A$2:$A$6','name':'=Sheet1!$C$1'})
chart.add_series({'values': '=Sheet1!$D$2:$D$6', 'categories':'=Sheet1!$A$2:$A$6','name':'=Sheet1!$D$1'})
chart.add_series({'values': '=Sheet1!$E$2:$E$6', 'categories':'=Sheet1!$A$2:$A$6','name':'=Sheet1!$E$1'})

chart.set_title({'name': u'년도별 바다 강수량'})
chart.set_x_axis({'name': u'년도'})
chart.set_y_axis({'name': u'강수량'})
worksheet.insert_chart('G2', chart)
excel_chart.save()
print("Chart Save")