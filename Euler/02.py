# Problem 02 - Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return b
def euler02():
    result, n = 0, 0
    while True:
        f = fib(n)
        if f > 4000000:
            print(result)
            break
        elif not f % 2:
            result += fib(n)
        n += 1
euler02()


# better fib function

def fibonacci(n):
    return fib(n)[0]
def fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
           return (d, c + d)
print(fibonacci(1000000))
