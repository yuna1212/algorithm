"""
시작 시간: 2022년 6월 30일 오후 5시
소요 시간: 20분
풀이 방법:
    크루스칼 알고리즘 연습!
    이해는 했는데 이제는 그냥 코드 외우고있는 기분이다,,,
"""
from sys import stdin
import heapq
def get_input():
    global parent, heights
    edges = [] # (weight, v1, v2)
    n, m = map(int, stdin.readline().split())
    
    parent = [i for i in range(n+1)]
    heights = [0] * (n+1)
    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        heapq.heappush(edges, (c, a, b))
    return edges

def find(u):
    global parent
    while u != parent[u]:
        u = parent[u]
    return u

def union(u, v):
    global parent, heights
    u, v = find(u), find(v)
    if u == v: return
    if heights[u] > heights[v]:
        parent[v] = u
    else:
        parent[u] = v
        if heights[u] == heights[v]:
            heights[v] += 1

# 크루스칼 알고리즘 시작
edges = get_input()
max_cost = -1
ret = 0
while edges:
    weight, u, v = heapq.heappop(edges)
    if find(u) == find(v) : continue
    union(u, v)
    ret += weight
    max_cost = weight
print(ret-max_cost)