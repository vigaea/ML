import numpy as np
import pandas as pd

data = pd.read_csv(r'D:/DATA/ML/mnist_train.csv')
print(data.shape)
print('data({0[0]},{0[1]})'.format(data.shape))
print(data.head())

labels_num = data.ix[:,0].ravel()
labels_count = np.unique(labels_num)
print(labels_num)
print('labels_num({0})'.format(len(labels_num)))
print(labels_count)

# a = np.array([[1,2,3],[4,5,6]])
# print(a)
# b = a[:,0]
# print(b)