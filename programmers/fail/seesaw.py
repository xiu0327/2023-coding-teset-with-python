from collections import defaultdict

# link : https://school.programmers.co.kr/learn/courses/30/lessons/152996


def solution(weights):
    answer = 0
    conditions = [1, 2, 1/2, 3/2, 2/3, 3/4, 4/3]
    dictionary = defaultdict(int)
    for weight in weights:
        for condition in conditions:
            answer += dictionary[weight * condition]
        dictionary[weight] += 1
    return answer


print(solution([100, 180, 360, 100, 270]))
