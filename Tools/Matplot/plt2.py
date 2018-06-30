import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('D:\\DATA\\ML\\UNRATE.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize=(6,3))  # figsize长和宽
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c='green')
plt.show()

fig1 = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    startm = i * 12
    endm = (i+1) * 12
    subset = unrate[startm:endm]  # 起始和结束的月份
    label = str (1948 + i)
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=label)
plt.legend(loc='best')  # 说明图的位置
plt.show()