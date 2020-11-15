import numpy as np


def find_nearest(random_array, value):
    array = np.asarray(random_array)
    index = (np.abs(array - value)).argmin()
    return array[index]
array = np.random.random(100)
print(array)
value = 0.5
print(find_nearest(array, value))

