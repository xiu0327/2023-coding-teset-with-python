from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people:
        if len(people) == 1: return answer + 1
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
        else: people.pop()
        answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))


# 효율성 실패 코드

# def solution(people, limit):
#     answer = 0
#     people = sorted(people)
#     while people:
#         # 1. 가장 가벼운 사람 한명 구함
#         first = people.pop(0)
#         # 2. 제한 무게를 넘지 않고, 가장 무거운 사람 한명 구함
#         for i in reversed(range(len(people))):
#             if people[i] + first <= limit:
#                 people.pop(i)
#                 break
#         answer += 1
#     return answer
