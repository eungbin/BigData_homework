#_*_coding:utf-8 _*_
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:.2f}'.format
AllData = pd.read_excel('./KobeBryant.xlsx')

grouped = AllData['shot_made_flag'].groupby(AllData['combined_shot_type'])

shotSuccess = AllData.groupby('combined_shot_type')[['shot_made_flag']].sum()
shotSuccess['tryCount'] = grouped.count()
shotSuccess['successRate'] = shotSuccess['shot_made_flag']/shotSuccess['tryCount']*100

xLabelList=['Bank shot','Dunk','Hook Shot','Jump Shot','Layup','Tip Shot']
index = range(len(xLabelList))
plt.xlabel('Shot Type');
plt.ylabel('Shot Success Rate')
plt.title('Kobe Bryant Shot Success Rate by Shot type')
plt.bar(index, shotSuccess['successRate'], tick_label = xLabelList)
plt.figure()
sns.heatmap(data = AllData.corr(), annot=True, fmt = '.2f', linewidths=.5, cmap='Blues')
plt.show()
