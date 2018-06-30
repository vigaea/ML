import numpy as np

vector = np.array([5, 10, 15, 20])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45],[11, 22, 33]])
print(vector)
print(matrix)

print(vector.dtype)
print(vector.shape) #一维的 = 打印出元素个数

print(matrix.shape)
print(matrix[:,1])
print(matrix[:,0:2])


mat1 = np.array([5, 10, 15, 20])
mat2 = np.array([
                [5, 10, 15],
                [20, 25, 30],
                [35, 40, 45]
             ])
print(mat1)
print(mat2)

print(mat1.sum())
print(mat2.sum(axis=0)) #按列
print(mat2.sum(axis=1)) #按行


