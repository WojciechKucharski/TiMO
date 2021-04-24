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
            maxIter: int = 10 ** 5,
            HMCR: float = 1.0,
            PAR: float = 1.0,
            BW: float = 0.1,
            HMSize: int = 10):  # Harmony Search - passing param.
        self.maxIter = maxIter
        self.HMCR = HMCR
        self.PAR = PAR
        self.BW = BW

        self.HMSize = HMSize



        self.valHistory = []  # clear history
        self.bestHistory = []
        self.iter = 0

        self.fun = fun
        self.varDim = 0
        for i in range(1, 6):  # evaluating function dimension
            if f"x{i}" in self.fun:
                self.varDim = i
        self.cube = cube
        self.HM, self.HMValues = [], []

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
            self.add(self.iteration())
            self.valHistory.append(0)  # value
            self.bestHistory.append([0, 0])  # coordinates
            if self.iter >= self.maxIter:
                break

        return f"Iteration overflow \nHarmony Search Stop: Iterations:{self.iter} \nBest solution: {self.HM[self.bestID][:-1]} \nValue: {self.HM[self.bestID][-1]}"

    @property
    def bestID(self):
        tmp = 0
        for i in range(len(self.HM)):
            if self.HM[tmp][-1] > self.HM[i][-1]:
                tmp = i
        return tmp
    def add(self, new):
        tmp = self.bestID
        if self.HM[tmp][-1] > new[-1]:
            self.HM[tmp] = new

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

