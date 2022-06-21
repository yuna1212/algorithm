"""
시작 시간: 2022년 6월 22일 오전 1시 45분
소요 시간: 30분
풀이 방법: BFS로 품
"""
from sys import stdin
def get_next_point(x, y, width):
    s = x*width + y + 1
    return s // width, s % width
def update(x, y, farm_map):
    if not (0 <= x < len(farm_map) and 0<= y < len(farm_map[0])):
        return False
    if farm_map[x][y] == 0:
        return False
    
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if 0 <= x < len(farm_map) and 0<= y <len(farm_map[0]):    
            if farm_map[x][y] == 1:
                farm_map[x][y] = 0
                stack.append((x+1, y))
                stack.append((x-1, y))
                stack.append((x, y+1))
                stack.append((x, y-1))
    return True
def solution():
    ret = 0
    # 데이터 입력
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    farm_map = [[0]*n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, stdin.readline().split())
        farm_map[x][y] = 1
    
    x, y = 0, 0
    while x < m and y < n:
        if update(x, y, farm_map):
            ret += 1
        x, y = get_next_point(x, y, n)
    return ret

for _ in range(int(input())):
    print(solution())
    