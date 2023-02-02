from collections import deque


# link : https://school.programmers.co.kr/learn/courses/30/lessons/154540

def solution(maps):
    answer = []

    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'X' or visited[i][j]: continue
            start = (i, j)
            queue = deque([start])
            visited[i][j] = True
            sum_ = int(maps[i][j])
            while queue:
                x, y = queue.popleft()
                for direction in directions:
                    dx = x + direction[0]
                    dy = y + direction[1]
                    if 0 <= dx < n and 0 <= dy < m:
                        if maps[dx][dy] != 'X' and not visited[dx][dy]:
                            sum_ += int(maps[dx][dy])
                            queue.append((dx, dy))
                            visited[dx][dy] = True
            answer.append(sum_)
    if answer: return sorted(answer)
    return [-1]




print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
