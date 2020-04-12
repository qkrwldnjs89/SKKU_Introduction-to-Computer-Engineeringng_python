# recursion

# factorial
def factorial(n):
    if n == 1:
        return 1
    elif n > 1:
        return factorial(n - 1) * n
print(factorial(5))

'''
n = 5
factorial(5)
= factorial(4) * 5
= factorial(3) * 4 * 5
= factorial(2) * 3 * 4 * 5
= factorial(1) * 2 * 3 * 4 * 5
= 1 * 2 * 3 * 4 * 5
'''

# Fibonacci
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: return fib(n - 1) + fib(n - 2)
