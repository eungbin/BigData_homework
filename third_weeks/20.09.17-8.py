import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5))
print(s)

s = pd.Series(np.random.randn(5), index=['A', 'B', 'C', 'D', 'E'])
print(s)

d = {'a': 0, 'b': 1, 'c': 2}
print(pd.Series(d))

data2 = [{'name': 'MARK'}, {'name': 'ERIC'}, {'name': 'JENNIFER'}]
df2 = pd.DataFrame(data2)
df2['age'] = [10, 11, 12]

print(df2)