import numpy as np
from src.function import Function
from src.curve import Node, Curve


def curve_simple(func: Function, n: int) -> Curve:
    curve = Curve()

    for k in range(n):
        x = func.a + k * (func.b - func.a) / (n - 1)
        y = func.evaluate(x)

        curve.add_node(Node(x, y))
    
    return curve

def range_repartition(function_rep: Function, n: int, lamda_placement: float, n_iter: int) -> np.array:
    X1 = np.linspace(function_rep.a, function_rep.b, n)
    for _ in range(n_iter):
        X2 = X1.copy()
        for k in range(1, n - 2):
            rep_1 = abs(function_rep.evaluate(X1[k]))
            rep_2 = abs(function_rep.evaluate(X1[k + 1]))
            
            if rep_1 > rep_2:
                X2[k + 1] = lamda_placement * X1[k] + (1 - lamda_placement) * X1[k + 1]
            else:
                X2[k] = lamda_placement * X1[k + 1] + (1 - lamda_placement) * X1[k]
        X1 = X2
    return X1


def curve_optimisation(func: Function, n: int, lamda_placement: float, n_iter: int) -> Curve:
    
    curve = Curve()

    for x in range_repartition(func.derivate().derivate(), n, lamda_placement, n_iter):
        y = func.evaluate(x)
        curve.add_node(Node(x, y))
    
    return curve
