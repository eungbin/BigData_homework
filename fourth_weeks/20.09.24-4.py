import pandas as pd
import numpy as np

tips = pd.read_csv('./4weeks_data/tips.csv')
tips = tips.sample(10)
print(tips)

grouped = tips['total_bill'].groupby(tips["smoker"])
means = tips['total_bill'].groupby(tips["smoker"]).mean()
# print(grouped)
# print(means)

randArray = np.random.randint(1, 10, len(tips))
print(randArray)
rMeans = tips.groupby(randArray).sum()
# print(rMeans)

# for day, smoker in grouped:
#     print(day)
#     print(smoker)

# for (key1, key2), group in tips.groupby(['smoker', 'day']):
#     print(key1, key2)
#     print(group.mean())

# eachGroup = dict(list(tips.groupby('day')))
# # print(eachGroup)
# # print(eachGroup['Sat'])
#
tip_dframe = tips.groupby('day')[['tip']].mean()    #Dataframe
print(tip_dframe)
#
# tip_series = tips.groupby('day')['tip', 'total_bill'].mean()    #Series
# print(tip_series)