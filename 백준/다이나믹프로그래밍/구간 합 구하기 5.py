"""
시작 시간: 2023-03-07 04:00 AM
소요 시간: 30분
풀이 방법: 다이나믹 프로그래밍, 블로그 풀이 참고
    - 원점 기준 넓이를 캐싱
    - (x1, y1, x2, y2)의 넓이는 (0, 0, x1, y1), (0, 0, x2, y2)의 넓이 조합들로 구함
"""
import sys
input = sys.stdin.readline

def solution(x1, y1, x2, y2):
    global AREA, GRID
    whole = AREA[x2][y2]
    overlapping = AREA[x1-1][y1-1] if x1 > 0 and y1 > 0 else 0 
    row = AREA[x1-1][y2] if x1 > 0 else 0
    column = AREA[x2][y1-1] if y1 > 0 else 0
    
    return whole - row - column + overlapping


n, m = map(int, input().rstrip().split())
GRID = []
for _ in range(n):
   GRID.append(list(map(int, input().rstrip().split())))

AREA = [[0]*n for _ in range(n)]
AREA[0][0] = GRID[0][0]
for i in range(1, n):
    AREA[0][i] += AREA[0][i-1] + GRID[0][i]
    AREA[i][0] += AREA[i-1][0] + GRID[i][0]

for i in range(1, n):
    for j in range(1, n):
        AREA[i][j] = AREA[i-1][j] + AREA[i][j-1] - AREA[i-1][j-1] + GRID[i][j]

for _ in range(m):
    print(solution(*map(lambda x: int(x) - 1, input().rstrip().split())))

