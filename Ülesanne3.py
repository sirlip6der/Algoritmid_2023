def fibonacci_recursive(a):
    if a <= 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibonacci_recursive(a - 1) + fibonacci_recursive(a - 2)