import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [0.5, 0.40, 0.35, 0.29, 0.24, 0.21, 0.17, 0.12]
p, v = np.polyfit(x, y, deg=2, cov=True)
q, g = np.polyfit(x, y, deg=1, cov=True)
a= np.arange(1, 8.01, 0.01)
sp = plt.subplot(121)
plt.errorbar(x, y, xerr=max(abs(v[0, 0]), abs(v[1, 0]), abs(v[2, 0])), yerr=max(abs(v[0, 1]), abs(v[1, 1]), abs(v[2, 1])))
w = np.poly1d(p)
plt.plot(a, w(a))
sp = plt.subplot(122)
plt.errorbar(x, y, xerr=max(abs(g[0,0]), abs(g[1, 0])), yerr=max(abs(g[1,1]), abs(g[0,1])))
o = np.poly1d(q)
plt.plot(a, o(a))
plt.show()