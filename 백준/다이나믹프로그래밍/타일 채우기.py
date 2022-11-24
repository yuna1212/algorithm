"""
시작 시간: 2022-11-24 02:55 PM
소요 시간: 1시간 10분
풀이 방법: 점화식 세우기 
"""
def solution():
    n = int(input())
    if n%2 == 1:
        return 0
    n //= 2
    dp = [0]*(n+1)
    dp[0], dp[1] = 1, 3
    for i in range(2, n+1):
        dp[i] = dp[i-1]*3 
        for j in range(0, i-1):
            dp[i] += dp[j]*2
    return dp[n]
print(solution())
