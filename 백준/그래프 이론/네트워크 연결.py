"""
시작 시간: 2022년 6월 30일 오후 3시 45분
소요 시간: 1시간
풀이 방법:
    크루스칼에 union find가 필수인가? 사이클이 생겼다는건 이미 방문한 노드 
    -> visited 배열로도 충분히 표현할 수 있을 것 같다. 다만 시간복잡도는 거의 비슷한데, 공간복잡도는 V배가 된다는게 문제
"""
from sys import stdin
import heapq
INF = 10000

def get_input():
    global parent, heights
    n = int(stdin.readline()) # vertex 개수
    m = int(stdin.readline()) # edge 개수
    edges = [] # (weight, vertex1, vertex2) vertex1과 vertex2는 weight만큼의 비용으로 연결되어있다.
    parent = [i for i in range(n+1)]
    heights = [0] * (n+1)
    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        heapq.heappush(edges, (c, a, b))
    return edges, n

def find(u):
    global parent
    while u != parent[u]:
        u = parent[u]
    return u

def union(u, v):
    global parent, heights
    u, v = find(u), find(v) # u와 v는 각각이 속한 그래프의 루트
    if u == v: return # 이미 같은 그래프

    if heights[u] > heights[v]: # u에 v를 포함한다: u가 더 높으니까
        parent[v] = u
    else:
        parent[u] = v # v에 u를 포함한다    
        if heights[u] == heights[v]:
            heights[v] += 1
    
# 크루스칼 알고리즘 시작
edges, vertex_count = get_input()
ret = 0
while edges:
    weight, v1, v2 = heapq.heappop(edges)
    if find(v1) == find(v2): continue # 사이클이 생김, 즉 이미 방문한 노드
    union(v1, v2)
    ret += weight
print(ret)