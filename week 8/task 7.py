import numpy as np
from numpy import loadtxt
x = np.arange(2, 75, 1)
np.savetxt('filename.dat', x, delimiter=',')
lines = loadtxt("filename.dat", delimiter=",")
print(lines)