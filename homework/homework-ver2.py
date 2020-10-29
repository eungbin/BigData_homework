#_*_coding:utf-8 _*_

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

font_location="C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False


file_name = './2012MonthlyTypeAccident.xlsx'
load_excel = pd.read_excel(file_name)

typeList = [u'차대사람', u'차대차', u'차량단독', u'철길건널목']
monthList = [u'1월', u'2월', u'3월', u'4월', u'5월', u'6월', u'7월', u'8월',
             u'9월', u'10월', u'11월', u'12월']

df = load_excel[[u'사고유형_대분류', u'월', u'1월', u'2월', u'3월', u'4월', u'5월',
                  u'6월', u'7월', u'8월', u'9월', u'10월', u'11월', u'12월']]
print(df)

for (key1, key2), group in df.groupby([u'사고유형_대분류', u'월']):
    if key2 == u'사망자수':
        print(key1, key2)
        print(type(group.sum()))

# acc_dframe = df.groupby(u'월')[monthList].sum() #DataFrame
#
# print(acc_dframe)


# def accident(type):
#     dataframe = df[(df[u'사고유형_대분류'] == type)]
#     dataframe_dead = dataframe[(dataframe[u'월'] == u'사망자수')]
#     dataframe_sum = pd.DataFrame(dataframe_dead.sum(), columns=[u'합계'])
#     dataframe_dead_sum = dataframe_dead.append(dataframe_sum.T)
#     dataframe_dead_sum.loc[u'합계', u'사고유형_대분류'] = type
#     dataframe_dead_sum.loc[u'합계', u'월'] = u'사망자수'
#     return dataframe_dead_sum.loc[u'합계']
#
#
# # 사고 유형이 차대사람인 행만 뽑아온다.
# car_person = df[(df[u'사고유형_대분류'] == u'차대사람')]
# # print(car_person)
#
# # 월이 사망자수인 행만 뽑아온다.
# car_person_dead = car_person[(car_person[u'월'] == u'사망자수')]
#
# # print(car_person_dead)
#
# car_person_sum = pd.DataFrame(car_person_dead.sum(), columns=[u'합계'])
# car_person_sum_df = car_person_dead.append(car_person_sum.T)
# # print(car_person_sum_df)
# car_person_sum_df.loc[u'합계', u'사고유형_대분류'] = typeList[0]
# car_person_sum_df.loc[u'합계', u'월'] = u'사망자수'
# print(car_person_sum_df)
# print(car_person_sum_df.loc[u'합계'])
# # print("test")
# columns_list = []
# for type in typeList:
#     columns_list.append(type)
#
# result = pd.DataFrame(index=range(0, monthList.__len__()))
# result.insert(0, "test", "")
# print(result)
#
# for i in range(0, 4):
#     result.loc[i] = accident(typeList[i])
#
# print(result)
# result.insert(0, "test", "")
# print(result)

# print(car_person_dead_sum)

# for row in df.values:
#     if row[1] == "사망자수":
#         if row[0] == "차대사람":
#             print(row)
#             car_person = [x+y for x,y in zip(car_person, row[2:])]
#             print(car_person)
#
#         if row[0] == "차대차":
#             print(row)
#             car_car = [x+y for x,y in zip(car_car, row[2:])]
#             print(car_car)
#
#         if row[0] == "차량단독":
#             print(row)
#             car_one = [x + y for x, y in zip(car_one, row[2:])]
#             print(car_one)
#
#         if row[0] == "철길건널목":
#             print(row)
#             train = [x + y for x, y in zip(train, row[2:])]
#             print(train)
#
# result = pd.DataFrame({u'test': '', typeList[0]: car_person, typeList[1]: car_car, typeList[2]: car_one, typeList[3]: train},
#                       index=monthList)
# print(result)
#
# def drawChart(data):
#     x = len(monthList)
#     x = np.arange(x)
#     bar_width = 0.35
#     y1 = data['차대사람']
#     y2 = data['차대차']
#     fix, ax = plt.subplots()
#     graph1 = ax.bar(x, y1, bar_width, label="차대사람")
#     graph2 = ax.bar(x+bar_width, y2, bar_width, label="차대차")
#     ax.set_xlabel(u'월')
#     ax.set_ylabel(u'사망자수')
#     ax.set_title(u'월별 차대사람/차대차 사망자 현황')
#     ax.set_xticks(x + bar_width/2)
#     ax.set_xticklabels(monthList)
#     ax.legend()
#     plt.show()
#
# drawChart(result)