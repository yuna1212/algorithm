"""
시작 시간: 2022-11-17 04:00 PM
소요 시간: 20분
풀이 방법: 간단한 dp
"""
n = int(input())
dp = [1]*10
for _ in range(n-1):
    for i in range(8, -1, -1):
        dp[i] = (dp[i] + dp[i+1]) % 10007
ans = 0
for n in dp:
    ans = (ans + n) % 10007
print(ans)
