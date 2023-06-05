# june 05 CS Fundamentals - Algo Strategies

def fibonacci(n, memo=None):
    if n == 0 or n == 1:
        return n
    
    if memo is not None:
        memo = memo
    else:
        memo = {}

    if n in memo:
        return memo[n]

    # return (fibonacci(n-1) + fibonacci(n-2))
    # return (fibonacci(n-1, memo) + fibonacci(n-2, memo))
    result = (fibonacci(n-1, memo) + fibonacci(n-2, memo))

    memo[n] = result
    print('this is my memo', memo)
    return result

# same results with below code
# use cache decorator
from functools import cache

rec_total_calls = 0
rec_calls_per_n = {}

def fibonacci(n, memo=None):
    if n == 0 or n == 1:
        return n
    
    if memo is not None:
        memo = memo
    else:
        memo = {}

    if n in memo:
        return memo[n]

    # return (fibonacci(n-1) + fibonacci(n-2))
    # return (fibonacci(n-1, memo) + fibonacci(n-2, memo))
    # result = (fibonacci(n-1, memo) + fibonacci(n-2, memo))
    return (fibonacci(n-1) + fibonacci(n-2))