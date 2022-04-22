"""
시작 시간: 2022년 4월 22일 오전 11시
소요 시간: 40분
풀이 방법:
    '트리의 지름' 1167 과 같은 문제이지만 부모노드가 무엇인지 제시함
    그렇다고 동일하게 height 구해서 풀었다가 recursion 에러
    그래서 BFS로 품
        - 아무 노드에서 가장 먼 노드 diameter_node 구하기
        - diameter_node에서 가장 먼 노드까지의 거리 구하기
        - 구한 거리가 트리의 지름
    
    많은 시간이 들지 않았다.
    왜냐하면 비슷한 문제를 풀어서 입력을 어떤 구조로 저장할지, 문제가 무슨 문제인지는 고민하지 않았기 때문이다.
"""
from sys import stdin

def make_tree():    
    n = int(input())
    # 인덱스는 노드 번호, 원소는 (직접 연결된 정점, 거리)의 리스트
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        parent, vertex, weight = tuple(map(int, stdin.readline().split()))
        tree[parent].append((vertex, weight))
        tree[vertex].append((parent, weight))
    return tree

def get_far_node_and_distance(node):
    global TREE
    stack = [(node, 0)]
    max_distance = 0
    far_node = 0
    visited = [False for _ in range(len(TREE))]
    while stack:
        node, distance = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        if distance > max_distance:
            max_distance = distance
            far_node = node
        children = TREE[node]
        for next, weight in children:
            stack.append((next, distance+weight))
    return far_node, max_distance
    

TREE = make_tree()
diameter_node, _ = get_far_node_and_distance(1)
_, diameter = get_far_node_and_distance(diameter_node)
print(diameter)