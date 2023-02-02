import sys
sys.setrecursionlimit(10000)


# link : https://school.programmers.co.kr/learn/courses/30/lessons/154540

def solution(maps):
    answer = []

    n = len(maps)
    m = len(maps[0])

    maps = [list(maps[index]) for index in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'X': continue
            answer.append(bfs(i, j, m, n, maps, 0))

    if answer: return sorted(answer)
    return [-1]


def bfs(i, j, m, n, maps, value):
    if i < 0 or i >= n or j < 0 or j >= m:
        return value
    if maps[i][j] == 'X':
        return value
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    value += int(maps[i][j])
    maps[i][j] = 'X'
    for direction in directions:
        dx = i + direction[0]
        dy = j + direction[1]
        value = bfs(dx, dy, m, n, maps, value)
    return value
