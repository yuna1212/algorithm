"""
시작 시간: 2022-10-13 05:35 PM
소요 시간: 20분
풀이 방법: 다익스트라
"""
import heapq
from sys import stdin
input = stdin.readline

def solution(area):
    visitings = []
    visited = [[False]*len(area) for _ in range(len(area))]
    weight, x, y = area[0][0], 0, 0
    diffs = ((0, 1), (1, 0), (-1, 0), (0, -1))
    while x != n-1 or y != n-1:
        for dx, dy in diffs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < len(area) and 0 <= ny < len(area):
                heapq.heappush(visitings, (weight + area[nx][ny], nx, ny))
        visited[x][y] = True
        while visited[x][y]:
            weight, x, y = heapq.heappop(visitings)
    return weight
        
problem_number = 1
while True:
    n = int(input().strip())
    if n == 0: break
    area = []
    for _ in range(n):
        area.append(list(map(int, input().strip().split())))
    print(f'Problem {problem_number}: {solution(area)}')
    problem_number += 1
