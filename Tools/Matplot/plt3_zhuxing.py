import matplotlib.pyplot as plt
import pandas as pd
from numpy import arange

reviews = pd.read_csv('D:\\DATA\\ML\\fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
nor_reviews = reviews[cols]
print(nor_reviews[0:1])

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = nor_reviews.ix[0, num_cols].values  # 柱形图的高度
bar_positions = arange(5) + 0.75  # 距零点的距离
fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)  #0.5/柱形的宽度
plt.show()


bar_widths = nor_reviews.ix[0, num_cols].values
fig,ax1 = plt.subplots()
ax1.barh(bar_positions, bar_widths, 0.3)  # 横向柱形图
ax1.set_yticklabels(num_cols)  # y轴每项的值
ax1.set_xlabel('Average rating')
ax1.set_ylabel('Sources')
plt.show()