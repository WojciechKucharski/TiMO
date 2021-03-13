import random as r
from function1 import f

class HM:
    def __init__(self, HMSize = 10, varDim = 2):
        self.HM = self.HMCreate(HMSize, varDim)
        self.eval = None
        self.fun = None

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
                new.append(r.random() * 200 - 100)
            new.append(None)
            HM.append(new)
        return HM

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

