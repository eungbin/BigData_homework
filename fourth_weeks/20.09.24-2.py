import pandas as pd
import numpy as np

df_A_B = pd.DataFrame({u'판매월': [u'1월', u'2월', u'3월', u'4월'],
                          u'제품A': [100, 150, 200, 130],
                          u'제품B': [90, 110, 140, 170]})

df_C_D = pd.DataFrame({u'판매월': [u'1월', u'2월', u'3월', u'4월'],
                           u'제품C': [112, 141, 203, 134],
                           u'제품D': [90, 110, 140, 170]})

df_Total = df_A_B.merge(df_C_D)
print(df_A_B)
print(df_C_D)
print(df_Total)


# merge는 공통된 열을 기준으로 통합된다. [ join과 다름 ]