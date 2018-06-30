import numpy as np

a = np.array([[1,2,3],[1,2,3]])
b = np.ones((np.shape(a)[0],1))
print(b)
print(a.shape[0])
print(np.ones((np.shape(a)[0],2)))
print(a.sum(axis=1))
print(np.tile(a,3))

mat = np.zeros((2, 3))
print(mat)