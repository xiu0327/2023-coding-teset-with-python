from collections import Counter


def solution(k, tangerine):
    answer = 0
    counts = sorted(list(Counter(tangerine).items()), key=lambda x: -x[1])

    for count in counts:
        if k <= 0: break
        _, cnt = count
        answer += 1
        k -= cnt
    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
