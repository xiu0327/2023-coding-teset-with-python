
# link : https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    dp = [0] * 2002
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 2001):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1234567

print(solution(4))