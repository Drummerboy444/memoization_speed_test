def list_factorial(numbers):
    results = []
    for n in numbers:
        results.append(factorial(n))
    return results

def factorial(n):
    if n is 0:
        return 1
    return n * factorial(n - 1)
 