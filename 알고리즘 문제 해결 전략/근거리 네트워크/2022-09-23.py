"""
시작 시간: 2022-09-23 05:00 PM
소요 시간: 40분
풀이 방법: 크루스칼로 품
"""
import heapq
def find(parents, u):
    if parents[u] == u: return u
    parents[u] = find(parents, parents[u])
    return parents[u]

def union(parents, rank, u, v):
    u, v = find(parents, u), find(parents, v)
    if u == v: return
    if u < v: u, v = v, u
    parents[v] = u
    if rank[u] == rank[v]: rank[u] += 1

def get_weight(u, v):
    return ((u[0]-v[0])**2 + (u[1]-v[1])**2)**0.5

def solution():
    n, m = map(int, input().split()) # 건물의 수, 케이블의 수
    positions = [ [] for _ in range(n) ]
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    for i in range(n):
        positions[i].append(xs[i])
    for i in range(n):
        positions[i].append(ys[i])

    # 기본 설정
    parents = [ i for i in range(n) ]
    rank = [1]*n
    a = None
    for _ in range(m):
        a, b = map(int, input().split())
        union(parents, rank, a, b)

    # 크루스칼
    ret = 0
    root = find(parents, a)
    heap = []
    for i in range(n):
        if root == parents[i]: continue
        for j in range(n):
            heapq.heappush(heap, (get_weight(positions[i], positions[j]), i, j))
    while heap:
        weight, u, v = heapq.heappop(heap)
        if find(parents, u) != find(parents, v):
            ret += weight
            union(parents, rank, u, v)
    return ret

for _ in range(int(input())):
    print('>>', solution())
