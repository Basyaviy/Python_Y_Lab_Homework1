import itertools


def bananas(s) -> set:
    result = set()
    # Your code here!
    etalon = "banana"
    r = len(etalon)
    my_list = list(s)

    group_indexes = list(itertools.combinations(range(len(my_list)), r))

    # писать исходное слово буквами из индексов, если такой буквы нет ставить прочерки
    for indexes in group_indexes:
        # шаблон ('-','-','-','-')
        list_word = ['-'] * len(my_list)
        just_word = ''

        for i in range(r):
            # слово с прочерками для результата
            list_word[indexes[i]] = my_list[indexes[i]]
            # слово собирается из индексов чтобы сравнить с эталоном
            just_word += my_list[indexes[i]]

        if just_word == etalon:
            word = ''.join(list_word)
            result.add(word)
    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}