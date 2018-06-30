import pandas as pd

data = [[1,2,3],[4,5,6]]
rows = ['a', 'b']
cols = ['c', 'd', 'e']
df = pd.DataFrame(data, index=rows, columns=cols)

print(df.loc['a'])  # 通过行标签索引 第一行所有列的数据
print('--------------------')

print(df.iloc[1])  # 通过 行号 索引数据
print('--------------------')

print(df.ix['a'])  # 通过 行标签或行号/ loc、iloc的混合
print(df.ix[0])