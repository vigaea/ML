import pandas as pd
import matplotlib.pyplot as plt
# hist 直方图

reviews = pd.read_csv(r'D:/DATA/ML/fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue']
norm_reviews = reviews[cols]
print(norm_reviews[:5])

fig, ax = plt.subplots()
# range为取值范围， bins为划分为多少个小区间
ax.hist(norm_reviews['Fandango_Ratingvalue'], range=(4,5), bins=20)
plt.show()

