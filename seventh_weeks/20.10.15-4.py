#_*_coding:utf-8 _*_

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location="C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

def drawChartOld(df):
    df2 = df[(df[u'2014_65rate'] >= 10)]
    y = df2[u'행정기관']
    x = df2[u'2014_65rate']
    plt.xlabel(u'행정기관')
    plt.ylabel(u'65세 이상 비율)')
    plt.title(u'2014년 65세 이상 비율이 10% 이상인  동네')
    plt.grid()
    plt.scatter(x, y)
    plt.show()

def drawChartAll(files):
    df = pd.read_excel(files)
    df2 = df.sum()
    x = ['2011','2012','2014']
    y = [df2[u'2011인구수'],df2[u'2012인구수'],df2[u'2014인구수']]
    y2 = [df2[u'2011_65'],df2[u'2012_65'],df2[u'2014_65']]
    fig, ax1 = plt.subplots()
    ax1.set_xlabel('년도')
    ax1.set_ylabel('전체 인구수', color='g')
    ax1.plot(x, y, 'g-')
    ax2 = ax1.twinx()
    ax2.plot(x, y2, 'b-')
    ax2.set_ylabel('65세 이상 인구 수', color='b')
    plt.title(u'년도별 성남시 전체 인구와 노령인구 비교')
    plt.grid()
    fig.tight_layout()
    plt.show()

excel_file_name = './Integration_seongnam2011_2014.xlsx'
df = pd.read_excel(excel_file_name)
drawChartAll(excel_file_name)
