import pandas as pd
import numpy as np

df1 = pd.DataFrame({'Class1': [95, 92, 98, 100],
                        'Class2': [91, 93, 97, 99]})
df2 = pd.DataFrame({'Class1': [87, 89],
                        'Class2': [85, 90]})

df3 = df1.append(df2)
df4 = pd.DataFrame({'Class3': [93, 91, 95, 98]})
df5 = pd.DataFrame({'Class4': [82, 92]})

print(df1)
print(df2)
print(df3)
print(df1.append(df2, ignore_index=True))       # append -> 아래로
print(df1.join(df4))                            # join -> 옆으로 [오른쪽]
print(df1.join(df5))