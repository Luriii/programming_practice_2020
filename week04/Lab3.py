import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-50, 50)
plt.plot(np.log((x**2+1)*np.exp(-abs(x)/10))/np.log(1+np.tan(1/(1+np.sin(x)*np.sin(x)))), lw=3, color="blue")
plt.show()