"""
시작 시간: 2022년 4월 7일 오후 1시 25분
소요 시간: 10분
풀이 방법:
    1부터 M까지, 각 금액에 대해 최소의 화폐 개수를 리스트에 저장
"""
n, m = map(int, input().split())
values = []
for _ in range(n):
    values.append(int(input()))
dp = [0]
for target in range(1, m+1):
    tmp = []
    for v in values:
        if target - v >= 0 and dp[target-v] > -1:
            tmp.append(dp[target-v]+1)
    if tmp:
        dp.append(min(tmp))
    else:
        dp.append(-1)
    
print(dp[-1])
