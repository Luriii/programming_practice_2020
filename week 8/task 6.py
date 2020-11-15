import numpy as np


def scale(x, xmin, xmax):
    a = (x-x.min(axis=0))*(xmax-xmin)
    b = x.max(axis=0) - x.min(axis=0)
    b[b==0] = 1
    return xmin + a/b

x = np.array([[ 0,  1],[ 2,  3],[ 4,  5],[ 6,  7],[ 8,  9],[10, 11],[12, 13],[14, 15]])
X_scaled = scale(x, 0, 1)
print(X_scaled)
