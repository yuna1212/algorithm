"""
시작 시간: 2022년 6월 30일 오후 5시 30분
소요 시간: 30분
풀이 방법:
    크루스칼 알고리즘 사용
    union에서 두 노드 받아서, root가 뭔지 찾고 처리해야하는 것에 주의
    트리와 트리를 합치는 거니까!
"""
from sys import stdin
import heapq
def get_dist(dot1, dot2):
    return ((dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2) ** 0.5
def get_input():
    global heights, parent
    n = int(input())
    vertexes = [] # (distance, v1, v2) v1과 v2는 distance만큼 떨어져서 서로 연결됨
    edges = []
    heights = [0] * n
    parent = [i for i in range(n)]
    for _ in range(n):
        x, y = map(float, stdin.readline().split())
        vertexes.append((x, y))
    for i in range(n):
        v1 = vertexes[i]
        for j in range(i+1, n):
            v2 = vertexes[j]
            dist = get_dist(v1, v2)
            heapq.heappush(edges, (dist, i, j))
            heapq.heappush(edges, (dist, j, i))
    return edges

def find(u):
    global parent
    while u != parent[u]:
        u = parent[u]
    return u
def union(u, v):
    global parent, heights
    u, v = find(u), find(v)
    if u == v: return # 이미 같이 이어짐
    if heights[u] > heights[v]:
        parent[v] = u
    else:
        parent[u] = v
        if heights[u] == heights[v]:
            heights[v] += 1

# 크루스칼 알고리즘 시작
edges = get_input()
ret = 0
while edges:
    dist, u, v = heapq.heappop(edges)
    if find(u) == find(v): continue
    union(u, v)
    ret += dist
print(round(ret, 2))