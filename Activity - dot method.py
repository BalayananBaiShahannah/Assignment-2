# 1
import numpy as np 

A = np.array([[0, 4], [2, 5]])
B = np.array([[9, 3], [1, 6]])

print(A)
print(B)

C = np.dot(A, B)
print("Dot product:")
print(C)


# 2
import numpy as np

A = np.array([[1, 0], [5, 1]])
B = np.array([[4, 2], [8, 9]])
C = np.array([[12, 7], [6, 10]])

print(A)
print(B)
print(C)

result = np.dot(np.dot(A, B), C)
print("Dot product with multiple matrices:")
print(result)


#3
import numpy as np

A = np.array([[1, 2, 1], [9, 1, 4], [6, 4, 10]])
B = np.array([[5, 10, 6], [7, 4, 8], [8, 7, 1]])
C = np.array([[9, 10, 12], [11, 0, 12], [9, 0, 7]])

print(A)
print(B)
print(C)

result = np.dot(np.dot(A, B), C)
print("Dot product with multiple matrices:")
print(result)

