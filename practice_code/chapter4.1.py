import math
import numpy
from numpy import *
import scipy.special
from scipy.special import yn_zeros,jn_zeros,yn,jn
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad, tplquad
from scipy import optimize
from pylab import *
import matplotlib.gridspec as gridspec


#matplotlib.rcParams.update({'font.size': 10, 'font.family': 'serif','text.usetex': True})

x=linspace(1,20,100)
y=x**2

fig1=figure()
axes1=fig1.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,x+1,color='blue',alpha=0.5,ls='-.')
axes1.plot(x,x,'g--',lw=3,marker='+',markersize=10,markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue")
axes1.plot(x,x-1,color='red',alpha=0.3,ls=':')

line,=axes1.plot(x,x-2,color='pink',ls='--')
line.set_dashes([5,10,15,10])

axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')

axes2=fig1.add_axes([0.2,0.6,0.3,0.2])
axes2.plot(y,x,'r--')
axes2.set_xlabel('x')
axes2.set_ylabel(r'$y=x^{2}$',fontsize=10,color='red')
for label in axes2.get_yticklabels():
    label.set_color('red')

axest=axes2.twinx()
axest.plot(y,x,'r--')
#axes2.set_xlabel('x')
axest.set_ylabel(r'$y=x^{2}$',fontsize=10,color='blue')
for label in axest.get_yticklabels():
    label.set_color('blue')

axes2.set_title('title')


fig2,axes3=plt.subplots(1,3)
for axi in axes3:


    axi.plot(x,y,'r.-',label='curve1')
    axi.set_xlabel(r'$x^22$')
    axi.set_ylabel('y')
    axi.set_title(r'$\alpha\times e^{33}$',fontsize=10)
    axi.legend(loc=3)

fig2.tight_layout()

fig3,axes4=plt.subplots(figsize=(4,4),dpi=100)
axes4.plot(x,x**3,x,x**2,'g--')
axes4.set_ylim([0,100])
axes4.set_xlim([0,20])
axes4.spines['right'].set_color("none")
axes4.yaxis.tick_left()

fig4,axes5=plt.subplots(figsize=(4,4),dpi=100)
axes5.plot(x,x**2,x,exp(x),'g--')

axes5.set_xlim([0,20])
axes5.set_yscale('log')
axes5.grid(True)
axes5.spines['bottom'].set_color('red')
axes5.spines['bottom'].set_linewidth(2)


fig5,axes6=plt.subplots(figsize=(10,4))
axes6.plot(x,x**2,x,x**3)
axes6.set_xticks([1,2,3,4,5])
axes6.set_xticklabels([r'$\alpha$',r'$\beta$',r'$\gamma$',r'$\delta$',r'$\epsilon$'],fontsize=10)
yticks = [0, 50, 100, 150]
axes6.set_yticks(yticks)
axes6.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=10)
axes6.set_ylim([0,150])
axes6.set_xlim([1,5])
axes6.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)





n = np.array([0,1,2,3,4,5])
xx = np.linspace(-0.75, 1., 100)

fig6, axes7 = plt.subplots(1, 4, figsize=(12,3))
axes7[0].scatter(xx, xx + 0.25*np.random.randn(len(xx)),color='pink')
axes7[0].set_title("scatter")

axes7[1].step(n, n**2, lw=2)
axes7[1].set_title("step")

axes7[2].bar(n, n**2, align="center", width=0.5, alpha=0.5,color='black')
axes7[2].set_title("bar")

axes7[3].fill_between(x, x**2, x**3, color="green", alpha=0.5)
axes7[3].set_title("fill_between")

fig6.tight_layout()


fig7 = plt.figure()
ax8 = fig7.add_axes([0.2, 0.2, .6, .6], polar=True)
t = np.linspace(0, 2 * np.pi, 100)
ax8.plot(t, t, color='blue', lw=3)

fig8 = plt.figure()
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2,0))
ax5 = plt.subplot2grid((3,3), (2,1))
fig8.tight_layout()

fig9 = plt.figure()
gs = gridspec.GridSpec(3, 3, height_ratios=[1,2,1], width_ratios=[1,2,1])
for g in gs:
    ax = fig9.add_subplot(g)
fig9.tight_layout()



show()







