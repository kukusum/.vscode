def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

factorial(5)

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

factorial(6)

