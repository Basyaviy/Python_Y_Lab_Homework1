def count_find_num(primesL, limit):
    # your code here
    my_set = set()
    result = 1
    # перемножаем primeL
    for i in primesL:
        result *= i

    if result <= limit:
        my_set.add(result)

        do_recursive(result, my_set)
        return [len(my_set), max(my_set)]
    return []


def do_recursive(source, my_set):
    for i in primesL:
        result = source * i
        if result <= limit:
            my_set.add(result)
            do_recursive(result, my_set)

        # primesL = [2, 3, 47]


# limit = 200
# print(count_find_num(primesL, limit))


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []