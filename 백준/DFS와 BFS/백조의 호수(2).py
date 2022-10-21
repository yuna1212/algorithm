"""
시작 시간: 2022-10-21 11:20 PM
소요 시간: 1시간
풀이 방법: 하루 전 지운 영역 근처만 탐색.. 여전히 시간초과
"""
import sys
input = sys.stdin.readline
def union(u, v):
    global PARENT_OF, RANK
    # u, v의 루트 찾기
    u = find(u)
    v = find(v)
    
    # 부모가 같다면 합칠 필요 없음
    if u == v: return

    # 깊이가 깊은게 u, 깊은게 낮은걸 포함
    if RANK[u] > RANK[v]:
        u, v = v, u
    PARENT_OF[v] = u

    # 깊이가 같았다면 u의 깊이를 1만큼 늘림
    if RANK[u] == RANK[v]:
        RANK[u] += 1
    return

def find(u):
    global PARENT_OF
    while u != PARENT_OF[u]:
        u = PARENT_OF[u]
    return u

def input_data():
    """ 입력 데이터 전역변수에 받고 백조 위치 return """
    global GRAPH
    GRAPH = []
    position_of_swans = []
    r, c = map(int, input().strip().split())
    for x in range(r):
        line = list(input().strip())
        for y in range(c):
            if line[y] == 'L':
                position_of_swans.append((x, y))
                line[y] = '.'
        GRAPH.append(line)
    return position_of_swans 

def is_valid(x, y):
    global GRAPH
    if 0 <= x < len(GRAPH) and 0 <= y < len(GRAPH[0]):
        return True
    return False

def get_adjacents(x, y):
    global GRAPH
    diff = ((0, 1), (1, 0), (-1, 0), (0, -1))
    ret = []
    for dx, dy in diff:
        nx, ny = x+dx, y+dy
        if is_valid(nx, ny):
            ret.append((nx, ny))
    return ret

def group_water(x, y, group_index):
    global GRAPH
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        # 검증
        if GRAPH[x][y] != '.': continue 
            
        GRAPH[x][y] = group_index
        for adjacent in get_adjacents(x, y):
            stack.append(adjacent)

def get_adjacent_water_index(x, y):
    global PARENT_OF, GRAPH
    diff = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    for nx, ny in get_adjacents(x, y):
        if GRAPH[nx][ny] != 'X':
            return GRAPH[nx][ny]
    return None

def set_melting_points(x, y, melting_points):
    """ 녹을 가능성이 있는 좌표와 결과를 저장할 리스트를 받아, 해당 위치가 녹을 수 있다면 (x, y, 물 그룹 번호) 원소 추가"""
    global GRAPH
    if GRAPH[x][y] == 'X':
        adjacent_water_index = get_adjacent_water_index(x, y)
        if adjacent_water_index is not None:
            melting_points.append((x, y, adjacent_water_index))

def melt_day(borders):
    global GRAPH
    melting_points = [] # melting_points[i] = [x, y, 물 그룹 번호]
    
    # 물과 맞닿은 경계 빙판을 melting_points에 저장 
    for x, y, _ in boarders:
        set_melting_points(x, y, melting_points)
        for nx, ny in get_adjacents(x, y):
            set_melting_points(nx, ny, melting_points)

    # 녹이기
    for x, y, water_index in melting_points:
        GRAPH[x][y] = water_index

    diff = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    for x, y, _ in melting_points:
        for nx, ny in get_adjacents(x, y):
            if GRAPH[nx][ny] != 'X':
                # 녹은 후, 물이 서로 맞닿아있다면 같은 group으로 처리
                union(GRAPH[x][y], GRAPH[nx][ny])
    return melting_points

# 데이터 초기화
swans = input_data()
water_index = 0
boarders = []
for i in range(len(GRAPH)):
    for j in range(len(GRAPH[0])):
        if GRAPH[i][j] == '.':
            group_water(i, j, water_index)
            water_index += 1
        else:
            boarders.append((i, j, -1))

# union find 구조 초기화
PARENT_OF = [ i for i in range(water_index) ]
RANK = [0]*water_index

swans_groups = [ GRAPH[x][y] for x, y in swans ]
day = 0
while find(swans_groups[0]) != find(swans_groups[1]):
    melt_day(boarders)
    day += 1
print(day)


