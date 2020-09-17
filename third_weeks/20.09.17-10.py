#_*_coding:utf-8 _*_
import pandas as pd
import numpy as np

KTX_data = {u'경부선 KTX': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
                u'호남선 KTX': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
                u'경전선 KTX': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
                u'전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
                u'동해선 KTX': [np.nan,np.nan, np.nan, np.nan, 2395, 3786, 6667]}
col_list = [u'경부선 KTX',u'호남선 KTX',u'경전선 KTX',u'전라선 KTX',u'동해선 KTX']
index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

df_KTX = pd.DataFrame(KTX_data, columns=col_list, index=index_list)
print(df_KTX)
print(df_KTX.head(3))
print(df_KTX.loc['2013':'2016'])

print(df_KTX.T)