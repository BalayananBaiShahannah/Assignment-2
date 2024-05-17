# 1
import numpy as np

A = np.array([[1, 2], [5, 6]])

A_inv = np.linalg.inv(A)
print("Inverse:")
print(A_inv)


# 2
import numpy as np

A = np.array([[4, 8, 3], [1, 5, 2], [0, 2, 10]])

A_inv = np.linalg.inv(A)
print("Inverse of matrix A:")
print(A_inv)


#3
import numpy as np

A = np.array([[1, 2, 4], [1, 2, 4]])
try:
    A_inv = np.linalg.inv(A)
    print("\nInverse of matrix A:")
    print(A_inv)
except np.linalg.LinAlgError:
    print("\nMatrix A is singular. Inverse does not exist.")



