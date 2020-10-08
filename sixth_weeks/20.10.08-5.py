import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import font_manager

font_location = "C:\\Windows\\Fonts\\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
city = [u'서울', u'인천', u'대전', u'대구', u'울산', u'부산', u'광주']

lat  = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16]
lon = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85]

pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995]
size = np.array(pop_den)*0.2
colors = ['r', 'g', 'b', 'c', 'm', 'k', 'y']

plt.scatter(lon, lat, s=size, c=colors, alpha=0.5)
plt.xlabel(u'경도(longtitude)')
plt.ylabel(u'위도(latitude)')
plt.title(u'지역별 인구 밀도(2017)')

for x, y, name in zip(lon, lat, city):
    plt.text(x, y, name)
plt.show()