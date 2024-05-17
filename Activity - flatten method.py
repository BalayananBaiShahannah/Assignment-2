#1
import numpy as np

A = np.array([[0, 2, 11], [5, 15, 4]])

A_flat = A.flatten()
print("Flattened matrix A:")
print(A_flat)


# 2
import numpy as np

A = np.array([[[1, 10, 3], [0, 5, 9]], [[17, 8, 29], [10, 1, 22]]])

A_flat = A.flatten(order='C')  # 'C' order (row-major)
print("Flattened array along the last two axes:")
print(A_flat)


#3
import numpy as np 

A = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

A_flat = A.flatten(order='F')  # 'F' order (column-major)
print("\nFlattened array with 'F' order:")
print(A_flat)

