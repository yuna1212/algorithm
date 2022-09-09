"""
시작 시간: 2022-09-09 PM 01:37
소요 시간: 1시간 40분
풀이 방법:
    - DP
    - 한칸 또는 두칸의 계단마다 밟고 지나가야 하는 조건 놓쳐서 시간 많이 소요,,
"""
import sys
input = sys.stdin.readline
def input_data():
    global STEPS, N
    STEPS = []
    N = int(input().strip())
    for _ in range(N):
        STEPS.append(int(input().strip()))

input_data()
dp = [0] * N 
dp[0] = STEPS[0] 
if N > 1:
    dp[1] = STEPS[0] + STEPS[1]
if N > 2:
    dp[2] = max(STEPS[0] + STEPS[2], STEPS[1] + STEPS[2])
if N > 3:
    for i in range(3, len(STEPS)):
        dp[i] = max(dp[i-2] + STEPS[i], dp[i-3] + STEPS[i-1] + STEPS[i])

print(dp[N-1])
