"""
시작 시간: 2022-11-24 04:18 PM
소요 시간: 1시간 
풀이 방법: BFS로 풀면 모든 경로(2^63) 탐색해야하므로 시간초과
    - DP로 푼다
    - 왼쪽에서 오른쪽, 위에서 아래로 한 칸씩 읽으면, 방문하는 칸까지의 경로는 부동으로 정해진다.
        - 음수의 이동은 없기 때문에
        - 이동은 오른쪽 혹은 아래방향이기 때문에
"""
n = int(input())
paths = [[0]*n for _ in range(n)]
grid = []
for _ in range(n):
    grid.append(tuple(map(int, input().strip().split())))
""" BFS -> 시간초과
stack = [(0, 0)]
diffs = ((1, 0), (0, 1))
while stack:
    x, y = stack.pop()
    if not (0 <= x < n) or not (0 <= y < n):
        continue
    paths[x][y] += 1
    if grid[x][y] == 0:
        continue
    stack.append((x, y+grid[x][y]))
    stack.append((x+grid[x][y], y))
"""
paths[0][0] = 1
for i in range(n):
    for j in range(n):
        if paths[i][j] == 0 or grid[i][j] == 0:
            continue
        if i + grid[i][j] < n:
            paths[i+grid[i][j]][j] += paths[i][j] 
        if j + grid[i][j] < n:
            paths[i][j+grid[i][j]] += paths[i][j] 
        
print(paths[n-1][n-1])
