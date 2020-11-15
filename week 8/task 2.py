import numpy as np

numbers = np.arange(2, 75, 1)
oddonly = [int(i) for i in numbers if i % 2 != 0]
for n, i in enumerate(numbers):
    if i % 2 != 0:
        numbers[n] = -1
print(numbers)
print(oddonly)
