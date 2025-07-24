import math
from .cache import cache

def calculate_fibonacci(n, a=None, b=None):
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    if n == 0:
        return 0
    if n == 1:
        return 1

    f1, f2 = 0, 1
    for _ in range(1, n + 1):
        f1, f2 = f2, f1 + f2

    return f2


@cache.memoize(timeout=60)
def compute_result(operation, a=None, b=None):
    # print(f"operation with: {a}, {b}")
    if operation == "pow":
        return math.pow(a, b)
    elif operation == "fibonacci":
        return calculate_fibonacci(int(a))
    elif operation == "factorial":
        return math.factorial(int(a))
    else:
        raise ValueError("Operation not supported")
