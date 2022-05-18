"""
시작 시간: 2022년 5월 18일 오후 5시 15분
소요 시간: 20분
풀이 방법:
    union find, 크루스칼 알고리즘 적용
"""
from sys import stdin
def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent) # 루트 바로 아래 모든 자식 노드들을 두게끔 한다.
    return parent[x]
def union(x, y, parent): # parent[i] = k  -->  i는 자식노드, k는 i의 부모노드
    parent[find(y, parent)] = find(x, parent) # 루트를 x로, 아래에 y를 둔다.


v, e = map(int, input().split()) # 정점 번호는 1 ~ v
edges = []
parent = [i for i in range(v+1)]
for _ in range(e):
    node_from, node_to, weight = map(int, stdin.readline().split())
    edges.append((node_from, node_to, weight))
edges.sort(key=lambda x: x[2]) # weight 기준으로 정점들 정렬

res = 0
for node1, node2, weight in edges:
    if find(node1, parent) == find(node2, parent):
        continue
    res += weight
    union(node1, node2, parent)
print(res)