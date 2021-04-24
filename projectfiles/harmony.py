import random as r
from function1 import f
import matplotlib.pyplot as plt
import numpy as np
import time


class HM:
    def __init__(self, fun: str = "x1^2+x2^2"):
        self.fun = fun
        self.iter = 0
        self.layersCreated = None

    def evaluate(self): #calculate function values for vectors in Harmony Memory
        self.eval = [] #clear evaluated values
        for x in self.HM:
            self.eval.append(f(self.fun, x)) #calculate values and put them to Array


    def HMCreate(self, HMSize: int = 10, start = 5): #create Harmony Memory with random Harmonies
        HM = [] #empty Harmony Memory
        for i in range(HMSize): #create given number of Harmonies
            H = [] #empty Harmony
            for j in range(self.varDim):
                H.append((r.random() * 2 - 1) * start) #initiate N "players" for single Harmony
            HM.append(H) #add Harmony to Harmony Memory
        self.HM = HM #save Harmony Memory
        return 1 #return 1 after success

    def iteration(self, HMCR = 1, PAR = 1, BW = 0.1, varRange = 25, *args, **kwargs): #do SINGLE iteration
        x = [] #initiate empty Harmony
        for i in range(self.varDim): #add N "players" to Harmony
            if r.random() < HMCR: #decide if generate new player or reuse other player from Harmony Memory
                x.append(r.choice(self.HM)[i]) #choose random player from Harmony Memory

                if r.random() < PAR: #decide if "player" will adjust
                    adjustment = (r.random() - 0.5) * 2 * BW
                    if adjustment + x[-1] < -varRange:
                        x[-1] = -varRange
                    elif adjustment + x[-1] > varRange:
                        x[-1] = varRange
                    else:
                        x[-1] += adjustment #adjusting "player"
            else:
                x.append((r.random() * 2 - 1) * varRange) #generate brand new "player"
        if f(self.fun, x) < self.worst[0]: #check if new Harmony is better than any Harmony in H. M.
            self.HM[self.worst[1]] = x #if yes, replace WORST Harmony in H. M. with new Harmony
        self.iter += 1 #add 1 to iteration counter

    def HarmonySearch(
            self, maxIter = 10**3, HMCR = 1, PAR = 1, BW = 0.1,
            HMSize = 10, startRange = 10, varRange = 10, plotHM = 0): #Harmony Search - passing param.

        self.HMCreate(HMSize, startRange)
        self.evaluate()

        self.TolXHistory = [] #clear history
        self.bestHistory = []
        self.iter = 0

        while True: #main Loop
            self.iteration(HMCR, PAR, BW, varRange) #execute iteration method
            self.evaluate() #evaluate values

            # add things to history
            self.TolXHistory.append(self.best[0]) #value
            self.bestHistory.append(self.best[2]) #coordinates

            if self.iter >= maxIter:  #stop crit. maxIter
                return f"Iteration overflow \nHarmony Search Stop: Iterations:{self.iter} \nBest solution: {self.best[2]} \nValue: {self.best[0]}"

    @property
    def varDim(self): #returns dimension of function imput aka Harmony Size
        dim = []
        for i in range(1, 6):
            if f"x{i}" in self.fun:
                dim.append(i)
        return max(dim)

    @property
    def TolXValue(self):
        return abs(self.worst[0] - self.best[0]) #dif. between best and worst


    @property
    def HMSize(self): #returns size of Harmony Memory
        return len(self.HM)

    @property
    def worst(self): #returns info about worst Harmony in Memory
        val = max(self.eval)
        id = self.eval.index(val)
        return [val, id, self.HM[id]]

    @property
    def best(self): #returns info about best Harmony in Memory
        val = min(self.eval)
        id = self.eval.index(val)
        return [val, id, self.HM[id]]

    def plotHistory(self): #draw a plot, where OX is iteration and OY is TolX value
        plt.plot(self.TolXHistory)
        plt.ylabel("fval")
        plt.xlabel("Iteration")
        plt.show()

    def createLayers(self, DZ):
        if self.layersCreated != DZ: #check if background XYZ is already created
            xlist = np.linspace(-DZ, DZ, int(DZ * 10))
            ylist = np.linspace(-DZ, DZ, int(DZ * 10))
            X, Y = np.meshgrid(xlist, ylist)
            Z = np.zeros((len(xlist), len(ylist)))
            for i in range(len(xlist)):
                for j in range(len(ylist)):
                    Z[-i - 1, -j - 1] = f(self.fun, [xlist[i], ylist[j]])

            self.layersCreated = DZ
            self.X = X
            self.Y = Y
            self.Z = Z

    def plotLayers(self, DZ = 5, his = False, HM = False, layers = 20):
        if self.varDim != 2:
            print("Can't draw layers")
            return 0

        self.createLayers(DZ)

        fig, ax = plt.subplots(1, 1)
        cp = ax.contourf(self.X, self.Y, self.Z, layers) #draw layers
        fig.colorbar(cp)
        ax.scatter(self.best[2][0], self.best[2][1], c="red")

        if his:
            x = flip(self.bestHistory)
            ax.plot(x[0], x[1])
        if HM:
            x = flip(self.HM)
            ax.scatter(x[0], x[1], c = "red")


        plt.ylabel("x2")
        plt.xlabel("x1")
        plt.show()

def flip(array):
    x = []
    y = []
    for i in array:
        x.append(i[0])
        y.append(i[1])
    return [x,y]