import random as r
from function1 import f
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple


class HM:
    def __init__(self):
        pass

    def HarmonySearch(
            self, cube: List[List[float]] = [[-5, 5], [-5, 5]],
            fun: str = "x1^2+x2^2",
            maxIter: int = 10 ** 3,
            HMCR: float = 1.0,
            PAR: float = 1.0,
            BW: float = 0.1,
            HMSize: int = 10,
            draw: bool = True):  # Harmony Search - passing param.

        self.maxIter = maxIter
        self.HMCR = HMCR
        self.PAR = PAR
        self.BW = BW
        self.HMSize = HMSize
        self.valHistory = []
        self.bestHistoryx1 = []
        self.bestHistoryx2 = []
        self.iter = 0
        self.fun = fun
        self.cube = cube

        self.varDim = 0
        for i in range(1, 6):  # evaluating function dimension
            if f"x{i}" in self.fun:
                self.varDim = i

        # sanity check
        if self.varDim < 2:  # checking function dimensions
            raise Exception("Function dimension too small")
        if self.varDim == 0:
            raise Exception("Function is invalid")

        if len(self.cube) < self.varDim:  # checking cube sizes
            raise Exception("Cube is to small, function has more arguments")
        for i in range(len(self.cube)):
            if len(self.cube[i]) < 2:
                raise Exception(f"Cube's argument no# {i} is incomplete")


        self.HM = self.HMCreate()
        while True:  # main Loop
            best, worst = self.best_worst
            self.valHistory.append(self.HM[best][-1])  # value
            if self.varDim == 2:
                self.bestHistoryx1.append(self.HM[best][0])
                self.bestHistoryx2.append(self.HM[best][1])
            if self.iter >= self.maxIter:
                break
            new = self.iteration()
            if new[-1] < self.HM[worst][-1]:
                self.HM[worst] = new

        if draw:
            self.plotHistory()
            if self.varDim == 2:
                self.plotLayers()
        return f"Iteration overflow \nHarmony Search Stop: Iterations:{self.iter} \nBest solution: {self.HM[best][:-1]} \nValue: {self.HM[best][-1]}"

    @property
    def best_worst(self):
        min, max = 0, 0
        for i in range(len(self.HM)):
            if self.HM[max][-1] < self.HM[i][-1]:
                max = i
            if self.HM[min][-1] > self.HM[i][-1]:
                min = i
        return min, max

    def iteration(self):  # do SINGLE iteration
        x = []  # initiate empty Harmony
        for i in range(self.varDim):  # add N "players" to Harmony
            if r.random() < self.HMCR:  # decide if generate new player or reuse other player from Harmony Memory
                x.append(r.choice(self.HM)[i])  # choose random player from Harmony Memory

                if r.random() < self.PAR:  # decide if "player" will adjust
                    adjustment = (r.random() - 0.5) * 2 * self.BW
                    if adjustment + x[-1] < self.cube[i][0]:
                        x[-1] = self.cube[i][0]
                    elif adjustment + x[-1] > self.cube[i][1]:
                        x[-1] = self.cube[i][1]
                    else:
                        x[-1] += adjustment  # adjusting "player"
            else:
                x.append(r.random() * abs(self.cube[i][0] - self.cube[i][1]) + self.cube[i][
                    0])  # generate brand new "player"
        x.append(f(self.fun, x))
        self.iter += 1

        return x  # return new Harmony

    def HMCreate(self):  # create Harmony Memory with random Harmonies
        HM = []  # empty Harmony Memory
        for i in range(self.HMSize):  # create given number of Harmonies
            H = []  # empty Harmony
            for j in range(self.varDim):
                H.append(r.random() * abs(self.cube[j][0] - self.cube[j][1]) + self.cube[j][
                    0])  # initiate N "players" for single Harmony
            H.append(f(self.fun, H))
            HM.append(H)  # add Harmony to Harmony Memory

        return HM  # save Harmony Memory


    def plotHistory(self):  # draw a plot, where OX is iteration and OY is TolX value
        plt.plot(self.valHistory)
        plt.ylabel("fval")
        plt.xlabel("Iteration")
        plt.show()

    def plotLayers(self, his: bool = True, HM: bool = False, layers: int = 50):
        if self.varDim != 2:
            print("Can't draw layers")
            return 0
        xlist = np.linspace(self.cube[0][0], self.cube[0][1], int(abs(self.cube[0][0]-self.cube[0][1]) * 10))
        ylist = np.linspace(self.cube[1][0], self.cube[1][1], int(abs(self.cube[1][0]-self.cube[1][1]) * 10))
        X, Y = np.meshgrid(xlist, ylist)
        Z = np.zeros((len(xlist), len(ylist)))
        for i in range(len(xlist)):
            for j in range(len(ylist)):
                Z[-i - 1, -j - 1] = f(self.fun, [xlist[i], ylist[j]])

        fig, ax = plt.subplots(1, 1)
        cp = ax.contourf(X, Y, Z, layers)  # draw layers
        fig.colorbar(cp)
        ax.scatter(self.bestHistoryx1[-1], self.bestHistoryx2[-1], c="red")

        if his:
            ax.plot(self.bestHistoryx1, self.bestHistoryx2)
        if HM:
            ax.scatter(self.bestHistoryx1, self.bestHistoryx2, c="red")

        plt.ylabel("x2")
        plt.xlabel("x1")
        plt.show()
