"""
시작 시간: 2022년 4월 28일 오후 1시 40분
소요 시간: 50분
풀이 방법:
    시간초과!
    
"""
def get_the_number_of_groups(ices):
    global N, M, UNITS
    the_number_of_groups = 0
    if not ices:
        return the_number_of_groups
    visited = [[True for _ in range(M)] for _ in range(N)]
    for x, y, _ in ices:
        visited[x][y] = False
    i = 0
    while i < len(ices):
        x, y, _ = ices[i]
        if visited[x][y]:
            i += 1
            continue
        stack = [(x, y)]
        the_number_of_groups += 1
        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in UNITS:
                nx, ny = x+dx, y+dy
                if 0<=nx<N and 0<=ny<M:
                    stack.append((nx, ny))
    return the_number_of_groups
        
        
from sys import stdin
UNITS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 데이터 입력
N, M = map(int, stdin.readline().split()) # 행, 열 개수
MAP = []
ices = []
for i in range(N):
    line = list(map(int, stdin.readline().split()))
    for j in range(M):
        if line[j] > 0:
            ices.append((i, j, line[j])) # 행, 열, 얼음 높이
    MAP.append(line)
year = 0
the_number_of_groups = get_the_number_of_groups(ices)

while the_number_of_groups < 2:
    next_ices = []
    for x, y, height in ices:
        adjacent_sea_count = 0
        for dx, dy in UNITS:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if MAP[nx][ny] == 0:
                    adjacent_sea_count += 1
        height -= adjacent_sea_count
        if height < 0:
            height = 0
        if height > 0:
            next_ices.append((x, y, height))
    for x, y, height in next_ices:
        MAP[x][y] = height
    ices = next_ices
    the_number_of_groups = get_the_number_of_groups(ices)
    year += 1
print(year)