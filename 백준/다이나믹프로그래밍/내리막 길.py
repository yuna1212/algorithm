"""
시작 시간: 2022-12-06 02:34 PM
소요 시간: 40분
풀이 방법: 길찾기에 DP를 적용해서 풀 때는, 다음으로 이동하기 전에 해당 위치까지 경로의 수를 가장 먼저 구할 방법 생각하기
    - 내리막길로 이동해야 하므로, 다음 위치로 이동하기 전 모든 경로를 구하기 위해서는 가장 큰 높이를 가진 길의 경로를 우선적으로 구해야 한다.
"""
import sys, heapq
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
heights = []
for _ in range(m):
    line = list(map(int, input().rstrip().split()))
    heights.append(line)

heap = [(-heights[0][0], 0, 0)] # 높이, x, y
ans = 0
diffs = ((-1, 0), (1, 0), (0, -1), (0, 1))
dp = [ [0] * n for _ in range(m) ]
dp[0][0] = 1
while heap:
    height, x, y = heapq.heappop(heap)
    height = -height

    if x == m - 1 and y == n - 1:
        # 목적지 도착
        break

    for dx, dy in diffs:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < m and 0 <= ny < n): continue

        if height > heights[nx][ny]:
            if dp[nx][ny] == 0:
                heapq.heappush(heap, (-heights[nx][ny], nx, ny))
            dp[nx][ny] += dp[x][y]
print(dp[m-1][n-1])
