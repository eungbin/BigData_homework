#_*_coding:utf-8 _*_

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager

font_location="C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

height = [100,120,130,140,150,160,170,180,190]
foot_size = [200,205,210,220,230,250,270,280,285]

plt.scatter(height,foot_size)
plt.xlabel(u'키 (cm)')
plt.ylabel(u'발사이즈(mm)')
plt.title(u'키에 따른 발 사이즈 차트')
plt.grid(True)
plt.show()
