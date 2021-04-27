from my_parser import f
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from typing import List, Tuple

def draw_contour(self, HM:bool, his:bool, cube: List[List[float]], fun: str, varDim: int = 0, layers: int = 250 ):

    if varDim != 2:
        print("Can't draw layers")
        return 0

    samples = int(max(abs(cube[1][0] - cube[1][1]), abs(cube[0][0] - cube[0][1])) * 10)
    xlist = np.linspace(cube[0][0], cube[0][1], samples)
    ylist = np.linspace(cube[1][0], cube[1][1], samples)
    X, Y = np.meshgrid(xlist, ylist)
    Z = np.zeros((len(xlist), len(ylist)))
    for i in range(len(xlist)):
        for j in range(len(ylist)):
            Z[-i - 1, -j - 1] = f(fun, [xlist[i], ylist[j]])

    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.25, bottom=0.25)

    cp = ax.contourf(X, Y, Z, layers)  # draw layers
    fig.colorbar(cp)
    #ax.scatter(self.bestHistoryx1[-1], self.bestHistoryx2[-1], c="red")
    if his:
        ax.plot(self.bestHistoryx1, self.bestHistoryx2)
    """
    if HM:
        ax.scatter(self.bestHistoryx1, self.bestHistoryx2, c="red")"""

    plt.ylabel("x2")
    plt.xlabel("x1")

    axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    sfreq = Slider(axfreq, 'Iteracja', 1, self.maxIter, valinit=self.maxIter, valstep=1)
    tmp1, tmp2 = vec(self.HMHistory[-1])
    H, = ax.plot(tmp1, tmp2, 'ro')
    def update(val):
        x = sfreq.val
        x1, x2 = vec(self.HMHistory[x])
        H.set_ydata(x2)
        H.set_xdata(x1)
    sfreq.on_changed(update)

    plt.show()

def vec(HMHis):
    x1 = []
    x2 = []
    for x in HMHis:
        x1.append(x[0])
        x2.append(x[1])
    return x1, x2

