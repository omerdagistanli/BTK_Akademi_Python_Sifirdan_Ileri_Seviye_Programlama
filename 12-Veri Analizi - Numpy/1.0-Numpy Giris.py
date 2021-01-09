# Normal listeler ile yapamadığımız birçok işi numpy ile yapabiliyoruz

import numpy as np

# list
py_list = [1,2,3,4,5,6,7,8,9]

# np array
np_array = np.array([1,2,3,4,5,6,7,8,9])

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)

print(py_multi)
print(np_multi)