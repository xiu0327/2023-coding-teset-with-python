from collections import Counter


def check_want_number(count, want, number) -> bool:
    for i in range(len(want)):
        if count[want[i]] != number[i]: return False
    return True


def solution(want, number, discount):
    answer = 0
    for day in range(len(discount)):
        count = Counter(discount[day:day + 10])
        if check_want_number(count, want, number): answer += 1
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))