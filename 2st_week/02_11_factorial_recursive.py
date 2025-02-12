def factorial(n):  # 5
    if n == 1:
        return 1
    return n * factorial(n - 1)


# factorial(n) = n * factorial(n-1) ...
# factorial(n - 1) = (n -1) * factorial(n-2) ...
# !5 = 5 * 4 * 3 * 2 * 1
print(factorial(5))
