from function1 import f
from harmony import HM
import numpy as np
import matplotlib.pyplot as plt


HMSize = 10
n = 2
#fun = "4*x1^2-2.1*x1^4+0.33*x1^6+x1*x2-4*x2^2+4*x2^4"
fun = "x1^2+x2^2+exp(x1)"

a = HM(HMSize, n, fun)

a.calc(32,  10000)

DZ = 3

xlist = np.linspace(-DZ, DZ, DZ * 10)
ylist = np.linspace(-DZ, DZ, DZ * 10)

X, Y = np.meshgrid(xlist, ylist)
Z = np.zeros((len(xlist), len(ylist)))
for i in range(len(xlist)):
    for j in range(len(ylist)):
        Z[-i-1, -j-1] = f(fun, [xlist[i], ylist[j]])


fig,ax=plt.subplots(1,1)
cp = ax.contourf(X, Y, Z)

fig.colorbar(cp)
ax.scatter(a.best[2][0], a.best[2][1], c = "red")
plt.show()