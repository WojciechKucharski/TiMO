from my_parser import f
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from typing import List, Tuple


def draw_contour(self, layers: int = 25):
    if self.varDim != 2:
        print("Can't draw layers")
        return 0
    samples = int(max(abs(self.cube[1][0] - self.cube[1][1]), abs(self.cube[0][0] - self.cube[0][1])) * 10)
    xlist = np.linspace(self.cube[0][0], self.cube[0][1], samples)
    ylist = np.linspace(self.cube[1][0], self.cube[1][1], samples)
    X, Y = np.meshgrid(xlist, ylist)
    Z = np.zeros((len(xlist), len(ylist)))
    for i in range(len(xlist)):
        for j in range(len(ylist)):
            Z[i, j] = f(self.fun, [ylist[j], xlist[i]])

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.25)

    cp = ax.contourf(X, Y, Z, layers)  # draw layers
    fig.colorbar(cp)
    #ax.plot(self.bestHistoryx[0], self.bestHistoryx[1])

    plt.ylabel("x2")
    plt.xlabel("x1")

    axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    sfreq = Slider(axfreq, 'Iteracja', 1, self.maxIter, valinit=self.maxIter, valstep=1)
    tmp1, tmp2 = vec(self.HMHistory[-1])
    H, = ax.plot(tmp1, tmp2, 'ro')
    G, = ax.plot(self.bestHistoryx[0][-1], self.bestHistoryx[1][-1], 'ro', color='green')

    def update(val):
        x = sfreq.val
        x1, x2 = vec(self.HMHistory[x])
        H.set_ydata(x2)
        H.set_xdata(x1)
        G.set_ydata(self.bestHistoryx[1][x])
        G.set_xdata(self.bestHistoryx[1][x])

    sfreq.on_changed(update)
    plt.show()


def vec(HMHis):
    x1 = []
    x2 = []
    for x in HMHis:
        x1.append(x[0])
        x2.append(x[1])
    return x1, x2
