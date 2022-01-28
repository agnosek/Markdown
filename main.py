def decimal_to_binary(n):
    if n == 1:
        return "1"
    if n == 0:
        return "0"
    else:
        return decimal_to_binary(n // 2) + str(n % 2)


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n
