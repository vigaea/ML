import numpy as np
group = np.array([[1.0, 1.1],[1.0,1.1],[0.0,0.0],[0.0,0.1]])
labels = ['A', 'B', 'C', 'D']
print(group)

mat = np.zeros(np.shape(group))
print(mat)

mat1 = np.array([1,20,5,2,3,6,87,9])  # --> (1,2,3,5,6,9,20,87)
print(mat1.argsort())