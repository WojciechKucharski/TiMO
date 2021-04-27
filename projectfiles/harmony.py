import random as r
from my_parser import f
import matplotlib.pyplot as plt
from typing import List, Tuple
from contour_plot import draw_contour


class HM:
    def __init__(self):
        pass

    def HarmonySearch(
            self, cube: List[List[float]] = [[-3, 3], [-3, 3]],
            fun: str = "2*x1^2-1.05*x1^4+x1^6/6+x1*x2+x2^2",
            maxIter: int = 10 ** 3,
            HMCR: float = 0.9,
            PAR: float = 0.9,
            BW: float = 0.1,
            HMSize: int = 10,
            draw: bool = True):  # Harmony Search - passing param.

        ########################################### User Given Variables
        self.maxIter = inRange(1, maxIter, 10 ** 6)
        self.HMCR = inRange(0.0, HMCR, 1.0)
        self.PAR = inRange(0.0, PAR, 1.0)
        self.HMSize = inRange(1, HMSize, 10 ** 3)
        self.BW, self.fun, self.cube, self.draw = BW, fun, cube, draw
        ########################################### Alg. Start Values
        self.HMHistory = []
        self.valHistory = []
        self.bestHistoryx1 = []
        self.bestHistoryx2 = []
        self.iter = 0
        ########################################### evaluating function dimension

        self.varDim = 0
        try:
            for i in range(1, 6):
                if f"x{i}" in self.fun:
                    self.varDim = i
        except Exception as e:
            return f"Failed to evaluate function dimension\n{e}"
        ########################################### sanity check
        if self.varDim < 2:  # checking function dimensions
            return "Function dimension too small"
        if self.varDim == 0:
            return "Function is invalid"

        if len(self.cube) < self.varDim:  # checking cube sizes
            return "Cube is to small, function has more arguments"
        for i in range(len(self.cube)):
            if len(self.cube[i]) < 2:
                return f"Cube's argument no# {i} is incomplete"

        ########################################### Harmony Search
        try:
            self.HM = self.HMCreate()  # initiate Harmony Memory
        except Exception as e:
            return f"Failerd to create Harmony Memory\n{e}"

        while True:  # main Loop
            self.HMHistory.append(self.HM.copy())
            try:
                best, worst = self.best_worst
            except Exception as e:
                return f"Failed to evaluate worst and best Harmony in iteration no# {self.iter}\n{e}"
            self.valHistory.append(self.HM[best][-1])  # value
            if self.varDim == 2:
                self.bestHistoryx1.append(self.HM[best][0])
                self.bestHistoryx2.append(self.HM[best][1])
            if self.iter >= self.maxIter:
                break
            try:
                new = self.iteration()
            except Exception as e:
                return f"Failed to execute iteration no# {self.iter}\n{e}"
            if new[-1] < self.HM[worst][-1]:
                self.HM[worst] = new
        response = f"Harmony Search Stop: Iterations:{self.iter} \nBest solution: {self.HM[best][:-1]} \nValue: {self.HM[best][-1]}"
        try:
            if self.draw:
                self.plotHistory()
                if self.varDim == 2:
                    self.plotLayers()
        except Exception as e:
            response += f"\nFailed to plot\n{e}"
        print(response)

        for i in range(len(self.valHistory)):
            response += "\n############################################"
            response += f"\nIteration {i}:\nBest point: [{self.bestHistoryx1[i]},{self.bestHistoryx2[i]}] \nf. value: {self.valHistory[i]}"
        return response

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

    def plotLayers(self):
        draw_contour(cube=self.cube,
                     varDim=self.varDim,
                     fun=self.fun,
                     layers=50,
                     self=self, HM=True, his=True)

def inRange(a, b, c):
    return min(c, max(a, b))
