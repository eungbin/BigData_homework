import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import numpy as np

font_location = "C:\\Windows\\Fonts\\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

x = np.arange(-4, 5, 0.5)

y = 2*x**2
plt.plot(x, y)
plt.title('y=x^2 Line 차트')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
