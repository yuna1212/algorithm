"""
시작 시간: 2022-09-20 11:24 PM
소요 시간: 40분
풀이 방법: N이 100이기 때문에 O(N^3)인 풀이도 통과할 수 있다.
"""
import sys
from collections import deque
input = sys.stdin.readline

DIFFS = ((0, 1), (0, -1), (1, 0), (-1, 0))
def bfs(area, rain):
    global DIFFS, N
    visited = [ [ False ]*N for _ in range(N)]
    ret = 0
    queue = deque()
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] > rain:
                queue.append((i, j))
                ret += 1
                while queue:
                    x, y = queue.popleft()
                    if not ( 0 <= x < N and 0 <= y < N): continue
                    if visited[x][y]: continue
                    visited[x][y] = True
                    if area[x][y] <= rain: continue
                    for dx, dy in DIFFS:
                        queue.append((x+dx, y+dy))

    return ret
                    
N = int(input().strip())
area = []
max_height = 0
for _ in range(N):
    row =  list(map(int, input().strip().split()))
    area.append(row)
    max_height = max(max_height, max(row))
    
max_group = 0
for rain in range(max_height):
    max_group = max(max_group, bfs(area, rain))
print(max_group)
