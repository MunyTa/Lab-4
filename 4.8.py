import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time:.6f} секунд")
        return result
    return wrapper

@timer
def factorial(n):
    from functools import reduce
    from operator import mul
    return reduce(mul, range(1, n + 1), 1)

print(factorial(500))