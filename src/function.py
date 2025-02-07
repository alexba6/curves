from scipy.integrate import quad

class Function:
    a: float
    b: float
    function: any

    def __init__(self, a: float, b: float, func: any):
        self.a = a
        self.b = b
        self.function = func
    
    def evaluate(self, x: int):
        assert self.a <= x and x <= self.b, "Invalide range"
        return self.function(x)

    def derivate(self):
        def derivate(x):
            dx = 10**(-5)
            return (self.function(x + dx) - self.function(x)) / dx
        return Function(self.a, self.b, derivate)
    
    def __add__(self, other):
        def inner(x):
            return self.evaluate(x) + other.evaluate(x)
        return Function(self.a, self.b, inner)
    
    def __sub__(self, other):
        def inner(x):
            return self.evaluate(x) - other.evaluate(x)
        return Function(self.a, self.b, inner)

    def abs(self):
        def inner(x):
            return abs(self.evaluate(x))
        return Function(self.a, self.b, inner)

    def integrate(self):
        return quad(lambda t: self.evaluate(t), self.a, self.b)