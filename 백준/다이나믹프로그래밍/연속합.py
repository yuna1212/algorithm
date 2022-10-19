"""
시작 시간: 2022-10-20 05:23 AM
소요 시간: 30분
풀이 방법: O(n^2) 시간초과
"""
n = int(input())
numbers = list(map(int, input().split()))
dp = numbers
ans = max(dp) 
for i in range(n):
    next_dp = []
    for j in range(n-i-1):
        element = dp[j]+numbers[j+i+1]
        ans = max(ans, element) 
        next_dp.append(element)
    dp = next_dp
print(ans)


