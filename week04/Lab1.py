import numpy as np
x = [1,10,1000]
for i in range(len(x)):
    y = (np.log(1 / np.e ** np.sin(x[i]) + 1) - (np.log((5 / 4) + 1 / x[i] ** 15))) / np.log(1 + x[i] ** 2)
    print("y(", x[i],')=', y)