import pandas as pd

data0 = [1, 3, 5, 7 ,9]
s = pd.Series(data0)

print(s)

data1 = {
    'year': [2016, 2017, 2018],
    'GDP rate': [2.8, 3.1, 3.0],
    'GDP': ['1.637M', '1.73M', '1.83M']
}
df = pd.DataFrame(data1)
print(df)

print(df['year'])
print(df.year)

print(df[df['year'] > 2016])

sum = df['GDP rate'].sum()
avg = df['GDP rate'].mean()
print(sum, avg)