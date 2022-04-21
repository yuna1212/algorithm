"""
시작 시간: 2022년 4월 21일 오후 4시 10분
소요 시간: 1시간 20분
풀이 방법:
    트리를 어떻게 표현할지 고민함
    각 서브트리의 높이를 구하는 것이 관건
"""
from sys import stdin
def make_tree():    
    v = int(input())
    # 인덱스는 노드 번호, 원소는 (직접 연결된 정점, 거리)의 리스트
    tree = [[] for _ in range(v+1)]

    parents_of = [0 for _ in range(v+1)]
    connection = [[] for _ in range(v+1)]
    parents_of[1] = -1
    for _ in range(v):
        line = tuple(map(int, stdin.readline().split()))
        vertex = line[0]
        for i in range(1, len(line)-1, 2):
            next, distance = line[i], line[i+1]
            connection[vertex].append((next, distance))

    stack = [1]
    while stack:
        parent = stack.pop()
        children = connection[parent]
        for child, distance in children:
            if parents_of[child] == 0:
                parents_of[child] = parent
                stack.append(child)
                tree[parent].append((child, distance))
    return tree
    
def get_height(root):
    max_height = 0
    global TREE, DIAMETER
    children = TREE[root]
    subtree_heights = []
    for child, dist in children:
        height = get_height(child) + dist
        subtree_heights.append(height)
    if subtree_heights:
        subtree_heights.sort()
        max_height = subtree_heights[-1]
        if len(subtree_heights) > 1:
            DIAMETER = max(DIAMETER, subtree_heights[-1]+subtree_heights[-2])
        else:
            DIAMETER = max(DIAMETER, subtree_heights[-1])
    return max_height
TREE = make_tree()
DIAMETER = 0
get_height(1)
print(DIAMETER)