"""
시작 시간: 2022년 6월 30일 오후 8시 30분
소요 시간: 1시간 30분
풀이 방법:
    크루스칼로 풀었다.
    테케가 이상한 꼴로 주어진다는걸 놓쳐서 시간 많이소요했다.
    그리고,
    
    union find가 "무방향" 그래프로 표현되는걸 잊지 말자. 진짜 집합,,
    그래서 정점 n1과 n2과 w로 연결되어 있다면, n2와 n1이 w로 연결된다는걸 따로 처리할 수 없다.
    오직 n1과 n2가 "연결되었음"을 표현한다!
    
    간선을 처리할 때 이전에는 우선순위큐(heap)을 사용했는데, 풀다보니까 그럴 필요가 없었다.
    우선순위큐를 사용한다면, 전체 큐를 모두 돌아야 하므로 삽입과 삭제에 걸리는 시간복잡도는 O(ElogE+VlogE)
    그냥 정렬한 후 스택으로 사용한다면, 삽입, 정렬, 삭제에 걸리는 시간복잡도는 O(E+ElogE+E) = O(ElogE+2E)
    거의 차이가 없긴 한데, 우선순위큐가 좀 더 좋긴 하네!
    
    암튼 이번엔 우선순위큐에 넣을 때 간선 하나를 2개씩 쪼개 넣어서 넣다가 시간 2배로 먹고 시간초과났다...주의하자
"""
from sys import stdin

def find(v):
    global parent
    while v != parent[v]:
        v = parent[v]
    return v

def union(v, u):
    global parent, heights
    v, u = find(v), find(u)
    if v == u: return
    
    if heights[v] > heights[u]:
        parent[u] = v
    else:
        parent[v] = u
        if heights[v] == heights[u]:
            heights[u] += 1

# 크루스칼 알고리즘 시작
while True:
    global heights, parent
    m, n = map(int, stdin.readline().split())
    if m == 0 and n == 0:
        break
    all_count = 0
    edges = []
    for _ in range(n):
        n1, n2, weight = map(int, stdin.readline().split())
        all_count += weight
        edges.append((weight, n1, n2)) # (weight, n2, n1)은 넣을 필요 없다
    edges.sort(reverse=True)
    
    heights = [0] * m
    parent = [i for i in range(m)]
    
    ret = 0
    while edges:
        weight, n1, n2 = edges.pop()
        if find(n1) != find(n2):
            union(n1, n2)
        else:
            ret += weight
    print(ret)