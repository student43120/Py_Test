def fibonaccie(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev = 0
    current = 1

    for i in range(2, n + 1):
        temp = prev + current
        prev = current
        current = temp

    return current
