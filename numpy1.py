import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.shape)

zeros = np.zeros((2, 3))
print(zeros)
# [[0. 0. 0.]
#  [0. 0. 0.]]

ones = np.ones((2, 3))
print(ones)
# [[1. 1. 1.]
#  [1. 1. 1.]]

full = np.full((2, 3), 7)     #7로 채우겠다 라는 의미.
print(full)
# [[7 7 7]
#  [7 7 7]]

arange_array = np.arange(0, 10, 2)   
print(arange_array)  # [0 2 4 6 8]  arange는 간격 지정.

linspace_array = np.linspace(0, 1, 5)
print(linspace_array)  # [0.   0.25 0.5  0.75 1. ]  #구간 지정.

array = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = array.reshape((2, 3))
print(reshaped_array)
# [[1 2 3]
#  [4 5 6]]

flattened = reshaped_array.flatten()
print(flattened)  # [1 2 3 4 5 6]

raveled = reshaped_array.ravel()
print(raveled)  # [1 2 3 4 5 6]  

