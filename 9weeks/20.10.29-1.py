#_*_coding:utf-8 _*_
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location="C:\\Windows\\Fonts\\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

def getTotalData(files, year):      # 연도별 전체데이터 합계
    year = year + u'계'
    FileData = pd.read_excel(files)
    totalData = pd.DataFrame({u'구분':FileData[u'구분'],u'유형':FileData[u'유형']})     # 구분, 유형 텍스트 뽑아내서 데이터프레임 생성
    print(totalData)
    print("-----------------------------------------------")
    totalData[year] =  FileData.sum(axis=1)     # 구분, 유형별 합계 계산
    print(totalData)
    print("-----------------------------------------------")
    sumResult = pd.DataFrame(totalData.sum())   # 위에서 구한 구분, 유형별 합계의 합계 즉, 전체 합계를 구함
    print(sumResult)
    print("-----------------------------------------------")
    sumRecord =  pd.DataFrame({u'구분':u'전체', u'유형':'전체',year:sumResult.T[year]})     # 전체합계 데이터프레임 생성
    print(sumResult)
    print(sumResult.T)
    print(sumResult.T[year])
    print(sumRecord)
    totalData = totalData.append(sumRecord, ignore_index=True)
    return totalData

def getNeedData(totalData, typeList, year):     #연도별 유형별 합계데이터
    year = year + u'계'
    chartData = totalData[(totalData[u'구분'] == u'강력범죄')]
    df = pd.DataFrame(chartData.sum()).T
    pieData = pd.DataFrame({u'유형':'강력범죄', u'유형별 합계':df[year]})
    for types in typeList:
        df = totalData[(totalData[u'구분'] == types)]
        df2 = pd.DataFrame(df.sum()).T
        record =pd.DataFrame({u'유형':types, u'유형별 합계':df2[year]})
        pieData = pieData.append(record, ignore_index=True)
    return pieData

totalData1 = getTotalData('./crime2012.xlsx', '2012')
totalData2 = getTotalData('./crime2016.xlsx', '2016')
typeList = [u'절도', u'폭력범죄',u'지능범죄',u'풍속범죄',u'특별경제범죄',u'마약범죄',u'보건범죄',u'환경범죄', u'교통범죄',u'노동범죄',u'안보범죄',u'선거범죄',u'병역범죄',u'기타']
addData1 = totalData1[(totalData1[u'구분'] == u'전체')]
addData2 = totalData2[(totalData2[u'구분'] == u'전체')]
pieData2012 = getNeedData(totalData1, typeList, '2012')
pieData2012 = pieData2012.append(pd.DataFrame({u'유형':u'전체', u'유형별 합계':addData1[u'2012계']}), ignore_index=True)
pieData2012[u'유형별 점유율'] = pieData2012[u'유형별 합계']/pieData2012.loc[15][u'유형별 합계']*100

pieData2016 = getNeedData(totalData2, typeList, '2016')
pieData2016 = pieData2016.append(pd.DataFrame({u'유형':u'전체', u'유형별 합계':addData2[u'2016계']}), ignore_index=True)
pieData2016[u'유형별 점유율'] = pieData2016[u'유형별 합계']/pieData2016.loc[15][u'유형별 합계']*100

pd.options.display.float_format = '{:.3f}'.format
pies1 = pd.DataFrame(pieData2012[0:15])
pies2 = pd.DataFrame(pieData2016[0:15])
plt.figure(figsize=(7,7))
plt.subplot(1,2,1)
plt.title(u'2012년 범죄 유형별 점유율')
plt.pie(pies1[u'유형별 점유율'], labels=pies1[u'유형'], autopct='%.3f%%')
plt.subplot(1,2,2)
plt.title(u'2016년 범죄 유형별 점유율')
plt.pie(pies2[u'유형별 점유율'], labels=pies2[u'유형'], autopct='%.3f%%')
plt.show()