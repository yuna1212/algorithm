"""
시작 시간: 2022-12-06 04:24 PM
소요 시간: 40분
풀이 방법: 반복되는 문제로 어떻게 쪼갤 수 있을지 생각하기
    - 덧셈의 순서가 다르면 다른 경우이다
        - ex. f(n = 4, k = 3)
            - case1. 가장 앞에 0을 더할 때: f(n = 4, k = 2)
            - case2. 가장 앞에 1을 더할 때: f(n = 3, k = 2)
            - case3. 가장 앞에 2을 더할 때: f(n = 2, k = 2)
            - case4. 가장 앞에 3을 더할 때: f(n = 1, k = 2)
            - case5. 가장 앞에 4을 더할 때: f(n = 0, k = 2)
            - case1 ~ 5에서 구한 값을 모두 더한다.
            - 이 때 각 경우는 중복되지 않으며, 순서가 다른 덧셈도 다른 경우로 취급하게 된다.
"""
n, k = map(int, input().split())
dp = [1]*(n+1)

for i in range(2, k+1):
    next_dp = [0]*(n+1)
    next_dp[0] = 1
    for j in range(1, n+1):
        for l in range(j+1):
            next_dp[j] = (dp[l] + next_dp[j]) % 1000000000
    dp = next_dp
print(dp[-1])
