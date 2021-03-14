from harmony import HM
import matplotlib.pyplot as plt
import numpy as np

fun = "4*x1^2-2.1*x1^4+0.33*x1^6+x1*x2-4*x2^2+4*x2^4"
#fun = "x1^2+x2^2"

if True:
    a = HM(fun)
    a.HarmonySearch(TolX = 3, maxIter = 5000, BW = 0.1, HMSize = 100, HCMR = 0.9, plotHM = 300)


