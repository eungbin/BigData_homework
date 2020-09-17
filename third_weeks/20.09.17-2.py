import numpy as np

a = np.zeros((2, 2))
print(a)

a = np.ones((2, 3))

print(a)

a = np.full((2, 3), 5)
print(a)

a = np.eye(3)
print(a)

a = np.array(range(20)).reshape((4, 5))
print(a)