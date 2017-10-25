import math
import numpy
from numpy import *
import scipy.special
from scipy.special import yn_zeros,jn_zeros,yn,jn
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad, tplquad
from scipy import optimize
from pylab import *



matplotlib.rcParams.update({'font.size': 18, 'text.usetex': True})

x=linspace(1,20,100)
y=x**2

fig, ax = plt.subplots()
ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('title')

show()


