from collections import deque


def solution(prices):
    n = len(prices)
    answer = []
    stack = deque(prices)

    while stack:
        present_price = stack.popleft()

        cnt = 0
        for stack_price in stack:
            if present_price > stack_price:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
            
    return answer


print(solution([1, 2, 3, 2, 3]))
