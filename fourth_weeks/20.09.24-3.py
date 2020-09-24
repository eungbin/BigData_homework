import pandas as pd

rainAmount = pd.read_csv('./4weeks_data/sea_rain.csv', encoding="utf8", sep="\t", index_col=u"년도")
print(rainAmount)

df_WH = pd.DataFrame({'Weight':[62, 67, 55, 74],
                          'Height':[165, 177, 160, 180]},
                           index=['ID_1', 'ID_2', 'ID_3', 'ID_4'])

df_WH.index.name = 'User'
bmi = df_WH['Weight']/(df_WH['Height']/100)**2
df_WH['BMI'] = bmi
print(df_WH)
df_WH.to_csv('./bmi.csv')