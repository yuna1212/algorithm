"""
시작 시간: 2022년 3월 25일 오후 5시 40분
소요 시간: 50분
풀이 방법:
    DFS로 해결: stack을 재귀로 만든다면 더 간단하게 구현됨
"""
# 데이터 받기
n, m = map(int, input().split())
ice_board = []
for _ in range(n):
    data = list(input())
    ice_board.append(list(map(int, data)))

# 내 solution
stack = []
start = 0
group = 0
delta_adjacents = ((0, 1), (0, -1), (1, 0), (-1, 0))
while start < n*m:
    start_x, start_y = start//m, start%m
    if ice_board[start_x][start_y]  == 0:
        # 시작 위치가 얼음
        group += 1
        for delta_x, delta_y in delta_adjacents:
            # 주변 조사
            adjacent_x, adjacent_y = start_x+delta_x, start_y+delta_y
            if 0<=adjacent_x<n and 0<=adjacent_y<m:
                adjacent = ice_board[adjacent_x][adjacent_y]
                if adjacent == 0:
                    # 주변이 얼음이면
                    stack.append((adjacent_x, adjacent_y))
                    ice_board[adjacent_x][adjacent_y] += 1
    
    start += 1
    while stack:
        ice_x, ice_y = stack.pop()
        for delta_x, delta_y in delta_adjacents:
            # 주변 조사
            adjacent_x, adjacent_y = ice_x+delta_x, ice_y+delta_y
            if 0<=adjacent_x<n and 0<=adjacent_y<m:
                adjacent = ice_board[adjacent_x][adjacent_y]
                if adjacent == 0:
                    # 주변이 얼음이면
                    stack.append((adjacent_x, adjacent_y))
                    ice_board[adjacent_x][adjacent_y] += 1
        
print(group)

# 모범 solution
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 주어진 범위 벗어나면 종료
    if x<= -1 or x >=n or y <= -1 or y >= m:
        return False
    # 아직 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상, 하, 좌, 우 재귀호출
        dfs(x-1, y) # 함수 호출해서 False 리턴당하나, 여기서 호출 안하나 큰차이x
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
# 모든 위치에 대해 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
