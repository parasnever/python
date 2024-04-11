def find_factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial_recursive( n - 1)
print(find_factorial_recursive(5))
