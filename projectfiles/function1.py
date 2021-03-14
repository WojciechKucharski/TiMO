import math

def f(function, args):

    if type(function) != type("string"):
        print("Function is not a string!")
        return None

    if len(args) < 1:
        print("Not enough arguments!")
        return None

    for x in args:
        try:
            x = float(x)
        except Exception as e:
            print("Something is wrong with arguments!")
            print(e)
            return None

    for x in range(len(args)):
        try:
            function = function.replace("x{}".format(x + 1), "args[{}]".format(x))
        except Exception as e:
            print("Something may be wrong with x{}!".format(x + 1))
            print(e)
    function = mathConv(function)
    return eval(function)


def mathConv(s):
    try:
        s = s.replace("^", "**")
    except Exception as e:
        print("Failed to add powers!")
        print(e)
    try:
        s = s.replace("log", "math.log")
        s = s.replace("log2", "math.log2")
        s = s.replace("log10", "math.log10")
        s = s.replace("sin", "math.sin")
        s = s.replace("cos", "math.cos")
        s = s.replace("tan", "math.tan")
        s = s.replace("exp", "math.exp")
        s = s.replace("sqrt", "math.sqrt")
        s = s.replace("pi", "math.pi")
    except Exception as e:
        print("Failed to add math functions!")
        print(e)
    return s