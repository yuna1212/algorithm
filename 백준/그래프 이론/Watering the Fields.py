"""
시작 시간: 2022년 7월 1일 오전 2시
소요 시간: 35분
풀이 방법:
    시간초과!
    -> c++로 똑같이 작성하니 통과됨. 파이썬 느린거 채점시스템에서 추가시간 안줘서 문제난듯
"""
import sys
input = sys.stdin.readline

def get_cost(point1, point2):
    return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2

def get_edges():
    global parents, heights
    n, c = map(int, input().split())
    parents = [i for i in range(n)]
    heights = [0] * n
    edges = []
    vertexes = []
    for i in range(n):
        v = tuple(map(int, input().split()))
        for j, other in enumerate(vertexes):
            cost = get_cost(v, other)
            edges.append((cost, i, j))
        vertexes.append(v)
    edges.sort()
    return edges, c # 엣지랑 최소 값

def find(v):
    global parents
    while v != parents[v]:
        v = parents[v]
    return v

def union(u, v):
    global parents, heights
    u, v = find(u), find(v)
    if u == v: return
    if heights[u] > heights[v]:
        parents[v] = u
    else:
        parents[u] = v
        if heights[u] == heights[v]:
            heights[v] += 1

# 크루스칼 시작
edges, min_cost = get_edges()
ret = 0
i = 0
for i, (cost, v, u) in enumerate(edges):
    if find(v) == find(u): continue
    if cost < min_cost: continue
    union(v, u)
    ret += cost

group = find(0)
is_successed = True
for i in range(len(parents)):
    if group != find(i):
        is_successed = False
        break
if is_successed:
    print(ret)
else:
    print(-1)