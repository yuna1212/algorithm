"""
시작 시간: 2022년 3월 28일 오후 7시 50분
소요 시간: 1시간 40분
풀이 방법:
    주어진 순서대로 짜서 품
    좌표 입력이 (0, 0)부터가 아니라 (1, 1)인걸 놓쳐서 시간 지연됨...
"""
from sys import stdin
from collections import deque
# 입력
n = int(input())
board = [[0 for _ in range(n+1)] for _ in range(n+1)]

k = int(input())
apples = []
for _ in range(k):
    x, y = map(int, stdin.readline().split())
    board[x][y] = 2
    
directions = deque()
l = int(input())
for _ in range(l):
    changing_time, direction = stdin.readline().split()
    changing_time = int(changing_time)
    if direction == "L":
        direction = -3
    else:
        direction = 3
    directions.append((changing_time, direction))

time = 0
head = (1, 1)
board[1][1] = 1
snake = deque()
snake.append(head)
direction = 3 # 시작은 세시방향
changing_time, next_direction = directions.popleft() # 방향 전환 시간, 전환 방향
while True:
    # 다음 머리 방향 구하기
    if changing_time == time:
        direction = (direction + next_direction) % 12
        if directions:
            changing_time, next_direction = directions.popleft()
    next = head
    if direction == 3:
        next = head[0], head[1]+1
    elif direction == 6:
        next = head[0]+1, head[1]
    elif direction == 9:
        next = head[0], head[1]-1
    elif direction == 0:
        next = head[0]-1, head[1]
    
    time += 1
    
    # 머리의 다음 위치가 벽이라면
    if next[0] < 1 or next[0] > n or next[1] < 1 or next[1] > n:
        break
    
    # 머리의 다음 위치가 몸이라면
    if board[next[0]][next[1]] == 1:
        break
    
    # 머리를 다음 위치로 옮길 수 있다면
    head = next
    is_apple = board[head[0]][head[1]]
    board[head[0]][head[1]] = 1
    snake.appendleft(head)
    if not is_apple:
        # 사과는 없었음
        tail = snake.pop()
        board[tail[0]][tail[1]] = 0 # 꼬리였던 부분 빔
    a = 0
print(time)        