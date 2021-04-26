import math
from functools import lru_cache
from typing import List, Tuple


def f(function: str, args: List[float]) -> float:
    return evaluation(function, tuple(args))


@lru_cache(maxsize=20)
def evaluation(function: str, args: Tuple[float]) -> float:
    for x in range(len(args)):
        function = function.replace(f"x{x + 1}", f"args[{x}]")
    function = mathConv(function)
    return eval(function)


def mathConv(s: str) -> str:
    s = s.replace("^", "**")
    S = ["log", "log2", "log10", "sin", "cos", "tan", "exp", "sqrt", "pi"]
    for x in S:
        s = s.replace(x, "math." + x)
    return s
