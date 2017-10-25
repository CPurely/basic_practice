import matplotlib
matplotlib.use('Qt5Agg') # or for example MacOSX
import matplotlib.pylab as plt
import numpy as np


print(matplotlib.rcsetup.all_backends)
fig, ax = plt.subplots()
t = np.linspace(0, 10, 100)
ax.plot(t, np.cos(t) * np.sin(t))
plt.show()