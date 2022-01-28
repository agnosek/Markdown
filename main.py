def decimal_to_binary(x):
    if x == 1:
        return "1"
    if x == 0:
        return "0"
    else:
        return decimal_to_binary(x // 2) + str(x % 2)


def factorial(x):
    if x == 0:
        return 1
    else:
        return factorial(x-1) * x
