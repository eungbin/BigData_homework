#_*_coding:utf-8 _*_

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import pandas as pd

font_location = "C:\\Windows\\Fonts\\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

path = u'./'
drink_df = pd.read_csv(path+"drinks.csv")
cols = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
corr = drink_df[cols].corr(method='pearson')
cols_view = ['beer', 'spirit', 'wine', 'total']
sns.set(font_scale=1.5)
hm = sns.heatmap(corr.values, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 15}, yticklabels=cols_view, xticklabels=cols_view)
plt.tight_layout()

sns.set(style='whitegrid', context='notebook')
sns.pairplot(drink_df[['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']], height=2.5)
plt.show()