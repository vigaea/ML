import numpy as np

mat1 = np.arange(10).reshape(2,5)
mat2 = np.array([[0, 1, 2, 3, 4],[5, 6, 7, 8, 9],[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]])
print(mat1)
print(mat1.shape[1])
print(mat1.ndim) #矩阵的维度

print(mat2)
print(mat2.ndim)

print(np.arange(0, 10, 3))


A = np.array([[1,2],[3,4]])
B = np.array([[1,2],[3,4]])
print(A.dot(B))
print(np.dot(A, B))

print(np.sqrt(B)) #开方

a = np.floor(10 * np.random.random((2,12))) #向下取整
print(a)
print(a.shape)
print(a.ravel()) # 矩阵展开成一维

print(np.hsplit(a,3))
print(np.hsplit(a,(3,4)))

b = np.floor(10 * np.random.random((12,2)))
print(np.vsplit(b,3))
