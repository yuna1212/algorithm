"""
시작 시간: 2023-02-13 04:56 PM
소요 시간: 2시간
풀이 방법: DFS와 백트래킹, 근데 마지막 케이스는 시간초과
    - 트리 깊이가 2500이고 노드는 4개의 자식을 가짐 -> O(N)에 대해 N = 2^5000 
    - 불가!
    - 깊이가 2500이어서 4^2500만큼의 공간을 탐색해야하는걸 놓쳤다..
"""
import sys
sys.setrecursionlimit(2500*4)
def update_path(x, y):
    global PATH, K, END, N, M

    distance = len(PATH)
    if not ( 0 < x <= N and 0 < y <= M):
        # 범위를 벗어남
        return False

    distance_to_end = abs(x - END[0]) + abs(y - END[1])
    if distance + distance_to_end > K:
        # K 내에 도착 못함
        return False

    if distance == K and (x, y) == END:
        # 딱 K일 때 도착함
        return True

    diffs = { 'd': (1, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0) }
    for direction in ('d', 'l', 'r', 'u'):
        dx, dy = diffs[direction]
        PATH.append(direction)
        arrived = update_path(x+dx, y+dy)
        if arrived:
            return True
        else:
            PATH.pop()

    return False

def solution(n, m, x, y, r, c, k):
    global N, M, K, PATH, END
    N, M, K = n, m, k
    PATH = []
    END = r, c

    arrived = update_path(x, y)
    if arrived:
        return ''.join(PATH)
    else:
        return "impossible"
