from itertools import combinations_with_replacement
from collections import defaultdict


def solution(n, info):
    score_dict = defaultdict(list)

    # 라이언이 n번의 화살을 쏘아 맞힌 과녁의 점수
    replacement = combinations_with_replacement(range(11), n)

    for scores in replacement:
        lion = [0] * 11
        for score in scores:
            lion[10-score] += 1
        apeach_score = 0
        lion_score = 0

        for i in range(11):
            if info[i] == lion[i] == 0: continue
            elif info[i] >= lion[i]: apeach_score += (10-i)
            else: lion_score += (10-i)
        if lion_score - apeach_score > 0: score_dict[lion_score - apeach_score].append(lion)
    try:
        answer = sorted(score_dict[max(list(score_dict.keys()))], key=lambda x: [-x[10-index] for index in range(11)])
        return answer[0]
    except ValueError:
        return [-1]

print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))