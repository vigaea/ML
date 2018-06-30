import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('D:\\DATA\\ML\\UNRATE.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])  # to_datetime转换成标准日期格式
print(unrate.head(10))

twelve1 = unrate[0:12]
plt.plot(twelve1['DATE'], twelve1['VALUE'])
plt.xticks(rotation=45)  # 倾斜45度
plt.xlabel('Month')  # x、y轴说明和标题
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()

