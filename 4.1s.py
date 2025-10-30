from functools import reduce

def compose(*functions):

    return reduce(lambda f, g: lambda x: f(g(x)), functions)

def add_one(x): return x + 1
def multiply_by_two(x): return x * 2
def square(x): return x ** 2

composed = compose(square, multiply_by_two, add_one)

result = composed(3)
print(f"compose(square, ×2, +1)(3) = {result}")  # ((3 + 1) * 2) ** 2 = 64