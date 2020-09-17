#_*_coding:utf-8 _*_
import pandas as pd
import numpy as np
table_data3 = {u'봄':  [256.5, 264.3, 215.9, 223.2, 312.8],
                   u'여름': [770.6, 567.5, 599.8, 387.1, 446.2],
                   u'가을': [363.5, 231.2, 293.1, 247.7, 381.6],
                   u'겨울': [139.3, 59.9, 76.9, 109.1, 108.1]}

columns_list = [u'봄', u'여름', u'가을', u'겨울']
index_list = ['2012', '2013', '2014', '2015', '2016']
df3 = pd.DataFrame(table_data3, columns=columns_list, index=index_list)

print(df3)
print("average\n", df3.mean())
print("standard variation\n", df3.std())
print("spring average\n", df3.mean(axis=1))
print("static summary\n", df3.describe())
