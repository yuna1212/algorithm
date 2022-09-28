"""
시작 시간: 2022-09-28 04:37 PM
소요 시간: 1시간 30분
풀이 방법:
"""
VERTICAL = 0
ACROSS = 1
HORIZONTAL = 2
n = int(input())
graph = []
for _ in range(n):
    line = input()
    graph.append(line.split())
dp = [ [[0, 0, 0] for _ in range(n)] for _ in range(n) ]
dp[0][1][HORIZONTAL] = 1

for r in range(n):
    for c in range(1, n):
        if graph[r][c] != '0': continue

        is_verticable, is_horizontable, is_acrossable = False, False, False
        if c + 1 < n and graph[r][c+1] == '0': is_horizontable = True
        if r + 1 < n and graph[r+1][c] == '0': is_verticable = True
        if is_horizontable and is_verticable and graph[r+1][c+1] == '0': is_acrossable = True
        
        # 가로로 놓여있을 때
        if dp[r][c][HORIZONTAL] > 0:
            if is_horizontable:
                dp[r][c+1][HORIZONTAL] += dp[r][c][HORIZONTAL]
            if is_acrossable:
                dp[r+1][c+1][ACROSS] += dp[r][c][HORIZONTAL]

        # 세로
        if dp[r][c][VERTICAL] > 0:
            if is_verticable:
                dp[r+1][c][VERTICAL] += dp[r][c][VERTICAL]
            if is_acrossable:
                dp[r+1][c+1][ACROSS] += dp[r][c][VERTICAL]

        # 대각선
        if dp[r][c][ACROSS] > 0:
            if is_horizontable:
                dp[r][c+1][HORIZONTAL] += dp[r][c][ACROSS]
            if is_verticable:
                dp[r+1][c][VERTICAL] += dp[r][c][ACROSS]
            if is_acrossable:
                dp[r+1][c+1][ACROSS] += dp[r][c][ACROSS]

print(sum(dp[n-1][n-1]))
