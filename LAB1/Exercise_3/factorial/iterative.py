def iterative(n):
    if n < 0:
        return None  
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
