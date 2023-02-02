from itertools import product


def solution(word):
    dictionary = dict()
    for i in range(1, 6):
        for item in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            dictionary["".join(item)] = 1
    dictionary = dict(zip(sorted(dictionary.keys()), [index for index in range(1, len(dictionary.keys()) + 1)]))
    return dictionary[word]


print(solution("AAAAE"))