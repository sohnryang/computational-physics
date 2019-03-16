import numpy as np
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
B = np.array([(2, 2, 3, 3), (3, 2, 3, 2), (2, 1, 2, 2)])
print(A)
print(A[1, 2])
print(B)
print(B[2, 1])
print(A * B)
