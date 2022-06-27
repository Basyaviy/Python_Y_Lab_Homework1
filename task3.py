import math


def zeros(n):
    # логарифм от нуля
    if n == 0:
        return 0

        # https://mathworld.wolfram.com/Factorial.html - trailing zeros
    base = 5
    k_max = math.log(n, base)

    my_sum = 0
    for k in range(1, 1 + math.floor(k_max)):
        my_sum += int(n / 5 ** k)
    return my_sum


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7