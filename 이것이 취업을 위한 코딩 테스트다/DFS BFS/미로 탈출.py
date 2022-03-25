"""
시작 시간: 2022년 3월 25일 오후 11시 45분
소요 시간: 50분
풀이 방법:
    - BFS
    - 미로 각 칸에, 해당 칸까지 도달하기 위해 거치는 최소 칸 수 적어둠
    - 목적지에 도착하면 끝
"""
from collections import deque
# 입력
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, list(input()))))

queue = deque()
queue.append((0, 0))
destination = (n-1, m-1)
deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while queue:
    now = queue.popleft()
    if now == destination:
        # 목적지에 도착했으면
        break
    x, y = now[0], now[1]
    if maze[x][y] >= 1:
        # 이동가능한위치면
        for delta_x, delta_y in deltas:
            next_x, next_y = x+delta_x, y+delta_y
            if 0<=next_x<n and 0<=next_y<m:
                # 주어진 미로 범위 내에서
                if maze[next_x][next_y] == 1:
                    # 이전 방문 경험이 없는 경우
                    maze[next_x][next_y] = maze[x][y] + 1
                    queue.append((next_x, next_y))
print(maze[n-1][m-1])
        
        
    