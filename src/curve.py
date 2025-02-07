from typing import Set, List
import numpy as np
import matplotlib.pyplot as plt
from src.function import Function

class Node:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Curve:
    nodes: List[Node]

    def __init__(self):
        self.nodes = list()
    
    def add_node(self, node: Node):
        self.nodes.append(node)
    
    def get_x(self):
        return np.array([
            node.x for node in self.nodes
        ])
    
    def get_y(self):
        return np.array([
            node.y for node in self.nodes
        ]) 

    def draw(self, ax: plt.Axes, label: str, color: str = 'black'):
        ax.plot(self.get_x(), self.get_y(), label=label, color=color, linewidth=2)  

    def scatter(self, ax: plt.Axes, label: str, color: str = 'black'):
        ax.scatter(self.get_x(), self.get_y(), label=label, color=color, linewidth=2)  

    def get_function(self) -> Function:
        n = len(self.nodes)
        def inner(x):
            for k in range(n):
                n_a = self.nodes[k]
                n_b = self.nodes[k + 1]
                if n_a.x <= x <= n_b.x:
                    return n_a.y + (x - n_a.x) * (n_b.y - n_a.y) / (n_b.x - n_a.x)
            return 0
        return Function(self.nodes[0].x, self.nodes[n - 1].x, inner)

        