import matplotlib.pyplot as plt
import matplotlib
import numpy as np

x = np.arange(-4, 5, 0.5)
y1 = 2*x**2
y2 = 5*x+2
y3 = 4*x**2 + 10

plt.plot(x, y1)
plt.plot(x, y2)
plt.figure()
plt.plot(x, y3)
plt.show()