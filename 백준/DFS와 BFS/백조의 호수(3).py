"""
시작 시간: 2022-10-27 02:56 AM
소요 시간: 40분
풀이 방법: 전체 한번씩만 방문하는데 5%에서 시간초과...
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

def melt_day(will_melting_positions):
    global GRAPH
    melting_positions = will_melting_positions
    will_melting_positions = []
    while melting_positions:
        x, y = melting_positions.pop()
        if GRAPH[x][y] != 'X': continue
        adjacent_groups = []
        for nx, ny in get_adjacents(x, y):
            if GRAPH[nx][ny] == 'X':
                will_melting_positions.append((nx, ny))
            else:
                adjacent_groups.append(GRAPH[nx][ny])
        GRAPH[x][y] = adjacent_groups[0]
        if len(adjacent_groups) > 1:
            for group in adjacent_groups:
                union(GRAPH[x][y], group)
    return will_melting_positions

swans = input_data()
group_number = 0
will_melting_positions = []
for i in range(len(GRAPH)):
    for j in range(len(GRAPH[0])):
        if GRAPH[i][j] == '.':
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if GRAPH[x][y] == 'X':
                    will_melting_positions.append((x, y))
                    continue
                if GRAPH[x][y] != '.': continue
                GRAPH[x][y] = group_number
                for adjacent in get_adjacents(x, y):
                    stack.append(adjacent)
            group_number += 1

# union find 구조 초기화
PARENT_OF = [ i for i in range(group_number) ]
RANK = [0]*group_number

swans_groups = [ GRAPH[x][y] for x, y in swans ]
day = 0
while find(swans_groups[0]) != find(swans_groups[1]):
    will_melting_positions = melt_day(will_melting_positions)
    day += 1
print(day)

