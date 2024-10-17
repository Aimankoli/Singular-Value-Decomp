import numpy as np

matrix = np.matrix('1, 2, 1, 0; 2, 3, 10, 4; 1, 10, 1, 3; 0, 4, 3, 0')
print(np.linalg.matrix_rank(matrix))
# mt = matrix.T
# vals, vecs = (np.linalg.eig(mt@matrix))

u, s, v = np.linalg.svd(matrix)
print (u)
print("\n")
print(np.diag(s))
print("\n")
print(v)
print("\n")
print(np.dot(u, np.dot(np.diag(s),v)))