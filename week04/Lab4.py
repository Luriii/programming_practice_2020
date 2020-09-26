import matplotlib.pyplot as plt
y = input()
with plt.xkcd():
     plt.plot([eval(y) for x in range(75)], lw = 2, color="red")
plt.show()
