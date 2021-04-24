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
    s = s.replace("log", "math.log")
    s = s.replace("log2", "math.log2")
    s = s.replace("log10", "math.log10")
    s = s.replace("sin", "math.sin")
    s = s.replace("cos", "math.cos")
    s = s.replace("tan", "math.tan")
    s = s.replace("exp", "math.exp")
    s = s.replace("sqrt", "math.sqrt")
    s = s.replace("pi", "math.pi")
    return s
