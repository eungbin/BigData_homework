import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import font_manager
import pandas as pd

font_location = "C:\\Windows\\Fonts\\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
df_rain = pd.read_csv("./sea_rain.csv",encoding="utf8",sep="\t", index_col=u"년도")
print(df_rain)

fig1 = plt.figure()
ax1 = fig1.add_subplot(121)
rain_plot = df_rain.plot(grid = True, style = ['r--*', 'g-o', 'b:*', 'm-.p'], ax=ax1)
rain_plot.set_xlabel(u"연도")
rain_plot.set_ylabel(u"강수량")
rain_plot.set_title(u"연간 강수량")

temperature = [25.2, 27.4, 22.9, 26.2, 29.5, 33.1, 30.4, 36.1, 34.4, 29.1]
Ice_cream_sales = [236500, 357500, 203500, 365200, 446600, 574200, 453200, 675400, 598400, 463100]
dict_data = {u"기온":temperature, u"아이스크림 판매량":Ice_cream_sales}
df_ice_cream = pd.DataFrame(dict_data, columns=[u'기온', u'아이스크림 판매량'])
ax2 = fig1.add_subplot(122)
df_ice_cream.plot.scatter(x=u'기온', y=u'아이스크림 판매량', grid=True, title=u'최고 기온과 아이스크림 판매량', ax=ax2)

fig2 = plt.figure()
grade_num = [5, 14, 12, 3]
students = ['A', 'B', 'C', 'D']
df_grade = pd.DataFrame(grade_num, index=students, columns=['Student'])
ax3 = fig2.add_subplot(121)
grade_bar = df_grade.plot.bar(grid=True, ax=ax3)
grade_bar.set_xlabel(u"학점")
grade_bar.set_ylabel(u"학생수")
grade_bar.set_title(u"학점별 학생 수 막대 그래프")

math = [76,82,84,83,90,86,85,92,72,71,100,87,81,76,94,78,81,60,79,69,74,87,82,68,79]
df_math = pd.DataFrame(math, columns=['Student'])
ax4 = fig2.add_subplot(122)
math_hist = df_math.plot.hist(bins=8, grid=True, ax=ax4)
math_hist.set_xlabel(u"시험 점수")
math_hist.set_ylabel(u"도수(frequency)")
math_hist.set_title(u"수학 시험의 히스토그램")

fig3 = plt.figure()
fruit = [u'사과', u'바나나', u'딸기', u'오렌지', u'포도']
result = [7, 6, 3, 2, 2]
df_fruit = pd.Series(result, index=fruit, name=u"선택한 학생수")
explode_value = (0.1, 0, 0, 0, 0)
ax5 = fig3.add_subplot(111)
fruit_pie = df_fruit.plot.pie(figsize=(5,5), autopct='%.1f%%', startangle=90, counterclock = False,
                              explode=explode_value, shadow=True, table=True, ax=ax5)
fruit_pie.set_ylabel("")
fruit_pie.set_title(u"과일 선호도 조사 결과")
plt.show()
