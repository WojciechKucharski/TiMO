import random as r
from function1 import f
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple


class HM:
    def __init__(self, cube: List[List[float]], fun: str = "x1^2+x2^2"):
        #variables
        self.fun = fun
        self.varDim = 0
        for i in range(1, 6): #evaluating function dimension
            if f"x{i}" in self.fun:
                self.varDim = i
        self.cube = cube
        self.HM, self.HMValues = [], []

        #sanity check
        if self.varDim < 2: #checking function dimensions
            raise Exception("Function dimension too small")
        if self.varDim == 0:
            raise Exception("Function is invalid")

        if len(self.cube) < self.varDim: #checking cube sizes
            raise Exception("Cube is to small, function has more arguments")
        for i in range(len(self.cube)):
            if len(self.cube[i]) < 2:
                raise Exception(f"Cube's argument no# {i} is incomplete")

    def evaluate(self):  # calculate function values for vectors in Harmony Memory
        for x in self.HM:
            try:
                self.eval.append(f(self.fun, x))  # calculate values and put them to Array
            except Exception as e:
                raise Exception(f"Failed to evaluate Harmony no# {x} \n{e}")

    def HMCreate(self, HMSize: int = 10):  # create Harmony Memory with random Harmonies
        HM = []  # empty Harmony Memory
        for i in range(HMSize):  # create given number of Harmonies
            H = []  # empty Harmony
            for j in range(self.varDim):
                H.append(r.random() * abs(self.cube[j][0] - self.cube[j][1]) + self.cube[j][0])  # initiate N "players" for single Harmony
            HM.append(H)  # add Harmony to Harmony Memory
        self.HM = HM  # save Harmony Memory

    def iteration(self, HMCR: float = 1.0, PAR: float = 1.0, BW: float = 0.1):  # do SINGLE iteration
        x = []  # initiate empty Harmony
        for i in range(self.varDim):  # add N "players" to Harmony
            if r.random() < HMCR:  # decide if generate new player or reuse other player from Harmony Memory
                x.append(r.choice(self.HM)[i])  # choose random player from Harmony Memory

                if r.random() < PAR:  # decide if "player" will adjust
                    adjustment = (r.random() - 0.5) * 2 * BW
                    if adjustment + x[-1] < self.cube[i][0]:
                        x[-1] = self.cube[i][0]
                    elif adjustment + x[-1] > self.cube[i][1]:
                        x[-1] = self.cube[i][1]
                    else:
                        x[-1] += adjustment  # adjusting "player"
            else:
                x.append(r.random() * abs(self.cube[i][0] - self.cube[i][1]) + self.cube[i][0])  # generate brand new "player"
        if f(self.fun, x) < self.worst[0]:  # check if new Harmony is better than any Harmony in H. M.
            self.HM[self.worst[1]] = x  # if yes, replace WORST Harmony in H. M. with new Harmony
        self.iter += 1  # add 1 to iteration counter

    def HarmonySearch(
            self, maxIter=10 ** 3, HMCR=1, PAR=1, BW=0.1,
            HMSize=10, startRange=10):  # Harmony Search - passing param.

        self.HMCreate(HMSize, startRange)
        self.evaluate()

        self.valHistory = []  # clear history
        self.bestHistory = []
        self.iter = 0

        while True:  # main Loop
            self.iteration(HMCR, PAR, BW)  # execute iteration method
            self.evaluate()  # evaluate values

            # add things to history
            self.valHistory.append(self.best[0])  # value
            self.bestHistory.append(self.best[2])  # coordinates

            if self.iter >= maxIter:  # stop crit. maxIter
                return f"Iteration overflow \nHarmony Search Stop: Iterations:{self.iter} \nBest solution: {self.best[2]} \nValue: {self.best[0]}"


    @property
    def HMSize(self) -> int:  # returns size of Harmony Memory
        return len(self.HM)

    @property
    def worst(self) -> list:  # returns info about worst Harmony in Memory
        val = max(self.eval)
        id = self.eval.index(val)
        return [val, id, self.HM[id]]

    @property
    def best(self) -> list:  # returns info about best Harmony in Memory
        val = min(self.eval)
        id = self.eval.index(val)
        return [val, id, self.HM[id]]

    def plotHistory(self):  # draw a plot, where OX is iteration and OY is TolX value
        plt.plot(self.valHistory)
        plt.ylabel("fval")
        plt.xlabel("Iteration")
        plt.show()