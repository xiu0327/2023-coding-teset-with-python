
# link : https://school.programmers.co.kr/learn/courses/30/lessons/150369


def solution(cap, n, deliveries, pickups):
    answer = 0
    items = []
    for i in range(n):
        items.append(deliveries[i] + pickups[i])
    items.reverse()
    max_cap = cap * 2

    i = 0
    while sum(items) > 0:
        answer += (n-i)
        for j in range(i, len(items)):
            if items[j] > 0:
                if items[j] >= max_cap:
                    items[j] -= max_cap
                    max_cap = cap * 2
                    if items[j] == 0: i += 1
                    break
                else:
                    max_cap -= items[j]
                    items[j] = 0
                    i += 1

    return answer * 2


print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
