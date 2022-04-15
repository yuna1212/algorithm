"""
시작 시간: 2022년 4월 15일 오전 10시 55분
소요 시간: 30분
풀이 방법:
    deepcopy 모듈이 무거워서 문제라고 생각해서 visited 배열을 따로 만들어서 처리함
    그래도 느림
"""
FISH_INF_SIZE = 7
from sys import stdin
from collections import deque
def get_distance(space, start, end, size):
    visited = [[False for _ in range(len(space))] for _ in range(len(space))]
    visited[start[0]][end[0]] = True
    queue = deque()
    queue.append(((start), 0))
    movings = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    while queue:
        (x, y), distance = queue.popleft()
        distance += 1
        for dx, dy in movings:
            nx, ny = x+dx, y+dy
            if 0<=nx<len(space) and 0<=ny<len(space):
                if (nx, ny) == end:
                    return distance
                if space[nx][ny] <= size:
                    queue.append(((nx, ny), distance))
                    visited[nx][ny] = True
    return

def get_fish_positions(space, baby_size):
    positions = []
    for i in range(len(space)):
        for j in range(len(space)):
            if 0< space[i][j] < baby_size:
                positions.append((i, j))
    return positions

def solution():
    n = int(input())
    grid_map = []
    x, y = -1, -1
    for i in range(n):
        line = list(map(int, stdin.readline().split()))
        grid_map.append(line)
        if 9 in line:
            x, y = i, line.index(9)
    cost = 0
    baby_size = 2
    small_fish_positions = get_fish_positions(grid_map, baby_size)
    ate_fish_count = 0
    while small_fish_positions:
        fish_distances = []
        for fish_position in small_fish_positions:
            distance = get_distance(grid_map, (x, y), fish_position, baby_size)
            if distance:
                fish_distances.append((fish_position, distance))
        if not fish_distances:
            return cost
        
        eating_position, distance = min(fish_distances, key=lambda x: x[1])
        cost += distance
        grid_map[x][y] = 0
        x, y = eating_position
        grid_map[x][y] = 9
        ate_fish_count += 1
        if ate_fish_count == baby_size:
            baby_size += 1
            ate_fish_count = 0
        small_fish_positions = get_fish_positions(grid_map, baby_size)
    return cost

print(solution())