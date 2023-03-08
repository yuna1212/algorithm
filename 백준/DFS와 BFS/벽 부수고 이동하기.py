"""
시작 시간: 2023-03-08 02:11 PM
소요 시간: 40분
풀이 방법: visited 검사보다 벽인지 검사하는게 먼저여야 함
    - 아예 불가능한 수를 visited에서 관리하지 않기 위해
    - 해당 위치까지 '정상' 도착 했을 때, 벽을 부순 이력이 있는지 없는지를 나눠서 visited에 저장
"""
from collections import deque

n, m = map(int, input().split())
grid = []

for _ in range(n):
    line = list(map(int, list(input())))
    grid.append(line)

visited = { True: set(), False: set() }
queue = deque([(0, 0, 1, False)])
answer = -1
diffs = ((1, 0), (0, 1), (-1, 0), (0, -1))
while queue:
    x, y, dist, broken = queue.popleft()
    if not 0 <= x < n or not 0 <= y < m:
        # 위치 유효성 검사 
        continue

    if x == n-1 and y == m-1:
        # 목적지인지 검사
        answer = dist
        break

    if grid[x][y] == 1:
        # 벽인지 검사
        if broken:
            continue
        broken = True

    if (x, y) in visited[broken]:
        # 방문한 위치인지 검사
        # 정상도착했는데 벽을 현재 부쉈는지 안부쉈는지 나눠서 확인
        continue
    visited[broken].add((x, y))

    dist += 1
    for dx, dy in diffs:
        nx, ny = x+dx, y+dy
        queue.append((nx, ny, dist, broken))

print(answer)
