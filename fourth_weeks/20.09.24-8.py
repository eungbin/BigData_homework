import pandas as pd

df = pd.read_excel(u'./4weeks_data/담당자별_판매량_통합.xlsx')
#해당 경로의 엑셀파일 load

print("---Total Sales---")
print(df)
print(u"----3분기 250이상 판매량----")
print(df[(df[u'3분기']>=250)])
#3분기 데이터중 250이 넘는 행들 출력
print(df.iloc[:,[0,3,4,5,6]])
#모든 행과 0, 3, 4, 5, 6번째 열 출력

product_name = u'핸드백'
handbag = df[(df[u'제품명'] == product_name)]
#제품명이 product_name[핸드백]인 행들
handbag_sum = pd.DataFrame(handbag.sum(axis=1), columns=[u'연간판매량'])
print(handbag)
print("test")
print(handbag_sum)
#각 핸드백의 1분기~4분기 합 [연간 판매량]
handbag_total = handbag.join(handbag_sum)
#위에서 구한 연간판매량을 join을 이용하여 옆에 붙임
print(handbag_total)

handbag_sum2 = pd.DataFrame(handbag_total.sum(), columns=[u'합계'])
print("test1")
print(handbag_sum2)
print(handbag_sum2.T)
handbag_total2 = handbag_total.append(handbag_sum2.T)
handbag_total2.loc[u'합계', u'제품명'] = product_name
handbag_total2.loc[u'합계', u'담당자'] = u'전체'
handbag_total2.loc[u'합계', u'지역'] = u'전체'

print(u"---- 핸드백의 분기별 판매량  ----")
print(handbag)
print(u"---- 지역별 연간 판매량만 보기  ----")
print(handbag_total.sort_values(by=u'연간판매량',ascending=True))
print(u"---- 핸드백 통합 판매량 보기  ----")
print(handbag_total2)