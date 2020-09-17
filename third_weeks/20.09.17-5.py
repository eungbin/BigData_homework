import numpy as np
list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(list)

bool_indexing_array = np.array([
    [False, True, False],
    [True, False, True],
    [False, True, False]
])


n = a[bool_indexing_array]
print(n)