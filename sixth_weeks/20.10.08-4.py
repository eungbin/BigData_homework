import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib import font_manager

font_location="C:\\Windows\\Fonts\\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

x = np.arange(0, 5, 1)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3

plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc')
plt.legend(['data1', 'data2', 'data3', 'data4'], loc=4)
plt.title(u'그래프 형식 지정 예제')
plt.xlabel(u'0에서 4까지 1씩 증가하는 X축 값')
plt.ylabel(u'y축 값')
plt.text(0, 4, u"문자열 출력")
plt.savefig('c:\\Temp\\saveFigTest1.png', dpi=100)
plt.show()