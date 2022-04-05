"""
시작 시간: 2022년 4월 5일 오후 5시 5분
소요 시간: 10분
풀이 방법:
    DP
"""
# 입력
n = int(input())
stored = list(map(int, input().split()))

if n == 1:
    print(stored[0])
elif n == 2:
    print(max(stored))
else:
    dp = [stored[0], max(stored[:2])]
    for i in range(2, n):
        dp.append(max(dp[i-1], dp[i-2]+stored[i]))
    print(dp[-1])        