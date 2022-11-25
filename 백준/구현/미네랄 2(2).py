"""
시작 시간: 2022-11-25 03:33 PM
소요 시간: 2시간 30분
풀이 방법: 효율적인 답 구하기(x) 끈질기게 구현하기. 완전 그냥 시뮬레이션
"""
import sys
input = sys.stdin.readline
CAVE = []
TO_RIGHT = 0
MINERAL='x'
BLANK = '.'
R, C = map(int, input().strip().split())
DIFFS = ((-1, 0), (1, 0), (0, -1), (0, 1))

def get_stopped_position(direction, height):
    x = R - height 
    y = 0
    dy = 1
    if direction != TO_RIGHT:
        y = C - 1
        dy = -1
    while 0 <= y < C:
        if CAVE[x][y] == MINERAL:
            return x, y 
        y += dy
    return x, y - dy

def get_splitted_cluster(stopped_x, stopped_y):
    if CAVE[stopped_x][stopped_y] == BLANK:
        return
    CAVE[stopped_x][stopped_y] = BLANK 
    visited= [[False]*C for _ in range(R)]

    for dx, dy in DIFFS:
        x, y = stopped_x+dx, stopped_y+dy
        if x < 0 or x >= R or y < 0 or y >= C: continue
        if visited[x][y]: continue

        stack = [(x, y)]
        cluster = set() 

        is_bottom = False

        while stack:
            x, y = stack.pop()
            if x < 0 or x >= R or y < 0 or y >= C: continue
            if CAVE[x][y] == BLANK: continue
            if visited[x][y]: continue
            if x == R-1:
                is_bottom = True

            visited[x][y] = True
            cluster.add((x, y))

            for dx, dy in DIFFS:
                stack.append((x+dx, y+dy))

        if is_bottom:
            cluster.clear()
        elif cluster:
            return cluster
    return

def get_falling_height(cluster):
    min_height = R
    for x, y in cluster:
        for h in range(x+2, R):
            if CAVE[h][y] == MINERAL:
                if (h, y) in cluster: continue
                min_height = min(min_height, h - x - 1)
            elif h == R - 1:
                min_height = min(min_height, h - x) 
            else:
                continue
            if min_height == 1:
                return 1
    return min_height 

def move(cluster, height):
    for x, y in cluster:
        CAVE[x][y] = BLANK 
    for x, y in cluster:
        CAVE[x+height][y] = MINERAL


for _ in range(R):
    CAVE.append(list(input().strip()))
n = int(input().strip()) # 막대 던진 횟수
stick_heights = list(map(int, input().strip().split()))
for i in range(n):
    stopped_x, stopped_y = get_stopped_position(i%2, stick_heights[i])
    cluster = get_splitted_cluster(stopped_x, stopped_y)
    if cluster:
        height = get_falling_height(cluster)
        move(cluster, height)
for line in CAVE:
    print(''.join(line))
