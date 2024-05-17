#1
import numpy as np

A = np.array([[1, 7, 3], [5, 4, 8]])

print(A)

A_transpose = np.transpose(A)
print("Transpose:")
print(A_transpose)


# 2
import numpy as np

A = np.array([[[1, 9, 0], [5, 7, 0]], [[4, 5, 2], [8, 10, 15]]])

print(A)

A_transpose = np.transpose(A, axes=(0, 2, 1))
print("Transpose along specific axes:")
print(A_transpose)


#3
import numpy as np

A = np.array([[[10, 2], [14, 3]], [[7, 1], [9, 11]]])

print(A)

A_transpose = np.transpose(A, axes=(2, 0, 1))
print("Transpose along specified axes:")
print(A_transpose)
