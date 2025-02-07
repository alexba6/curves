import matplotlib.pyplot as plt
import numpy as np
import math

from src.function import Function
from src.curve import Curve, Node
from src.representation import curve_simple, curve_derivate


def display_curve_comparaison(ax: plt.Axes, name: str, raw_function: Function, curve: Curve):
    N_SMOOTH = 1000
    # Curve
    ax.set_title(name)
    curve.scatter(ax, name, 'black')
    curve_function = curve.get_function()
    curve_simple(curve_function, N_SMOOTH).draw(ax, name, 'blue')

    # Raw function
    craw = curve_simple(raw_function, N_SMOOTH)
    craw.draw(ax, 'function', 'red')

    print(name, (curve_function - raw_function).abs().integrate())

def display_iter(ax: plt.Axes, raw_function: Function, N: int):
    LAMBDA = []
    ERROR = []
    for lamda in np.linspace(0, 1, 100):
        curve = curve_derivate(raw_function, N, lamda, 1)
        func = curve.get_function()
        error = (func - raw_function).abs().integrate()[0]
        LAMBDA.append(lamda)
        ERROR.append(error)
    ax.plot(LAMBDA, ERROR, color='blue')  
    k = 0
    for i in range(len(ERROR)):
        if ERROR[i] < ERROR[k]:
            k = i
    ax.axvline(x=LAMBDA[k], color='black')
    ax.set_title(f"error {LAMBDA[k]:.2f}")
    return LAMBDA[k]
    

if __name__ == '__main__':
    N = 20

    fig, axs = plt.subplots(3, 1, figsize=(15, 10))

    func = Function(1, 5, lambda t: 10 * (t - 1)*(t - 2)*(t - 3)*(t - 4)*(t - 5))
    
    l = display_iter(axs[2], func, N)

    display_curve_comparaison(axs[0], 'derivate', func, curve_derivate(func, N, l, 1))

    display_curve_comparaison(axs[1], 'simple', func, curve_simple(func, N))



    plt.show()