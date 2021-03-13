import random as r
from function1 import f

class HM:
    def __init__(self, HMSize = 10, varDim = 2, fun = None):
        self.start = 10
        self.HM = self.HMCreate(HMSize, varDim)
        self.eval = None
        self.fun = fun
        self.HMCR = 1
        self.PAR = 1
        self.bw = 0.1
        self.it = 0


    def HMCreate(self, HMSize = 10, varDim = 2):
        try:
            HMSize = int(HMSize)
            varDim = int(varDim)
        except Exception as e:
            print("Something went wrong, created 10x2 HM")
            print(e)
            HMSize = 10
            varDim = 2

        HM = []
        for i in range(HMSize):
            new = []
            for j in range(varDim):
                new.append(r.random() * 2 * self.start - self.start)
            HM.append(new)
        return HM

    def addFun(self, fun):
        try:
            fun = str(fun)
            self.fun = fun
        except Exception as e:
            print("Error, function not added.")
            print(e)

    def evaluate(self):
        if self.isfun == False:
            print("No function")
            return -1
        self.eval = []
        for x in self.HM:
            self.eval.append(f(self.fun, x))

    @property
    def isfun(self):
        if self.fun is None:
            return False
        return True

    @property
    def HMSize(self):
        return len(self.HM)

    @property
    def varDim(self):
        return len(self.HM[0])

    @property
    def worst(self):
        self.evaluate()
        val = max(self.eval)
        id = self.eval.index(val)
        return [val, id, self.HM[id]]

    @property
    def best(self):
        self.evaluate()
        val = min(self.eval)
        id = self.eval.index(val)
        return [val, id, self.HM[id]]

    def iteration(self):
        x = []
        for i in range(self.varDim):
            if r.random() < self.HMCR:
                x.append(r.choice(self.HM)[i])
                if r.random() < self.PAR:
                    x[-1]+=r.random()*self.bw
            else:
                x.append(r.random() * 2 * self.start - self.start)
        if f(self.fun, x) < self.worst[0]:
            self.HM[self.worst[1]] = x
        self.it += 1

    def calc(self, TolX, maxIter):
        TolX = 10**(-TolX)
        i = 0
        j = 0
        while True:
            i+=1
            self.iteration()
            a = self.worst[0]
            b = self.best[0]
            if abs(a-b) < TolX:
                j+=1
            if j > 1:
                print("TolX satisfied")
                print("Harmony Search Stop: Iterations:{}".format(i))
                print("Best solution: " + str(self.best[2]))
                break
            if i > maxIter:
                print("Iteration overflow")
                print("Harmony Search Stop: Iterations:{}".format(i))
                print("Best solution: " + str(self.best[2]))
                break

