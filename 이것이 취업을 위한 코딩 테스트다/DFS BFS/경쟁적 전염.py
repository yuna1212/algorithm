"""
시작 시간: 2022년 4월 5일 오후 1시 10분
소요 시간: 30분
풀이 방법:
    BFS
    큐에 바이러스 번호, 행위치, 열위치, 시간을 저장해둠
    맨 처음 바이러스 위치를 큐에 넣을 때, 바이러스 번호 작은 것 부터 넣기
"""
from collections import deque
# 입력
n, k = map(int, input().split())
grid = []
virus_positions = list() # (바이러스 번호, 행위치, 열위치, 시간)
for i in range(n):
    a_line = list(map(int, input().split()))
    grid.append(a_line)
    for j in range(len(a_line)):
        if a_line[j] > 0:
            virus_positions.append((a_line[j], i, j, 0))
virus_positions.sort()
virus_positions = deque(virus_positions)
s, x, y = map(int, input().split())

# 바이러스 전염
time = 0
deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while virus_positions:
    virus_number, virus_x, virus_y, time = virus_positions.popleft()
    if time >= s:
        break
    for dx, dy in deltas:
        next_x, next_y = virus_x+dx, virus_y+dy
        if 0<=next_x<n and 0<=next_y<n and grid[next_x][next_y] == 0:
            virus_positions.append((virus_number, next_x, next_y, time+1))
            grid[next_x][next_y] = virus_number
print(grid[x-1][y-1])