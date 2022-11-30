"""
시작 시간: 2022-11-30 11:28 PM
소요 시간: 10분
풀이 방법: 
    - 모든 상자를 앞에서부터 차례로 하나씩 골라 상자들에 넣어본다. 각 연산의 결과를 기억해 이후 연산에 사용한다.
    - 첫번째 상자부터 차례로 뒷 상자에 넣을 수 있는지 계산한다.
    - 계산 결과를 기억한다.
    - 두번째 상자부터 차례로 뒷 상자에 넣을 수 있는지 계산한다. 이때 기억한 결과를 이용한다
    - 반복
"""
n = int(input())
sizes = list(map(int, input().split()))
dp = [1]*n
for i in range(n):
    for j in range(i+1, n):
        if sizes[i] < sizes[j]:
            dp[j] = max(dp[i]+1, dp[j])
print(max(dp))
