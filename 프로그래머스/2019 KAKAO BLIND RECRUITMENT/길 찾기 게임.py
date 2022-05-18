"""
시작 시간: 2022년 5월 19일 오후 2시 30분
소요 시간: 3시간
풀이 방법:
    알고리즘 문제 해결 전략의 트리 순회 순서 변경과 비슷한 문제
    x축 오름차순으로 정렬하면 중위순회 결과가 된다.
    y축 내림차순으로 정렬해서 앞에서부터 순차탐색하면 루트를 찾을 수 있다.
    이를 통해 전위, 후위순위 결과를 찾는다.
    recurssion limit 세팅하는 것 잊지 말기
"""
import sys
sys.setrecursionlimit(1001)
def solution(nodeinfo):
    answer = [[]]
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1) # nodeinfo[i] = (x, y, 노드번호)
    nodeinfo_inordered = sorted(nodeinfo, key=lambda x: x[0])
    nodeinfo_y_decr = sorted(nodeinfo, key=lambda x:-x[1])
    
    preorder_result = []
    postorder_result = []
    preorder(nodeinfo_inordered, nodeinfo_y_decr, preorder_result)
    postorder(nodeinfo_inordered, nodeinfo_y_decr, postorder_result)
    
    return [preorder_result, postorder_result]
def preorder(nodeinfo_inordered, nodeinfo_y_decr, result):
    root = nodeinfo_y_decr[0]
    root_index = nodeinfo_inordered.index(root) # 처음부터 nodeinfo_inordered[root_index-1]는 왼쪽자식, nodeinfo_inordered[root+1]부터 끝까지는 오른쪽 자식
    left_subtree = nodeinfo_inordered[:root_index]
    right_subtree = nodeinfo_inordered[root_index+1:]
    
    # 왼쪽과 오른쪽 트리의 루트 위치 탐색
    left_root_index = -1
    right_root_index = -1
    if left_subtree:
        for i in range(len(nodeinfo_y_decr)):
            if nodeinfo_y_decr[i] in left_subtree:
                left_root_index = i
                break
    if right_subtree:
        for i in range(len(nodeinfo_y_decr)):
            if nodeinfo_y_decr[i] in right_subtree:
                right_root_index = i
                break
    
    result.append(root[2]) # 노드 번호 추가
    if left_root_index > -1:
        preorder(left_subtree, nodeinfo_y_decr[left_root_index:], result) # 왼쪽 트리 탐색
    if right_root_index > -1:
        preorder(right_subtree, nodeinfo_y_decr[right_root_index:], result) # 오른쪽 트리 탐색

def postorder(nodeinfo_inordered, nodeinfo_y_decr, result):
    root = nodeinfo_y_decr[0]
    root_index = nodeinfo_inordered.index(root) # 처음부터 nodeinfo_inordered[root_index-1]는 왼쪽자식, nodeinfo_inordered[root+1]부터 끝까지는 오른쪽 자식
    left_subtree = nodeinfo_inordered[:root_index]
    right_subtree = nodeinfo_inordered[root_index+1:]
    
    # 왼쪽과 오른쪽 트리의 루트 위치 탐색
    left_root_index = -1
    right_root_index = -1
    if left_subtree:
        for i in range(len(nodeinfo_y_decr)):
            if nodeinfo_y_decr[i] in left_subtree:
                left_root_index = i
                break
    if right_subtree:
        for i in range(len(nodeinfo_y_decr)):
            if nodeinfo_y_decr[i] in right_subtree:
                right_root_index = i
                break
    
    
    if left_root_index > -1:
        postorder(left_subtree, nodeinfo_y_decr[left_root_index:], result) # 왼쪽 트리 탐색
    if right_root_index > -1:
        postorder(right_subtree, nodeinfo_y_decr[right_root_index:], result) # 오른쪽 트리 탐색
    result.append(root[2]) # 노드 번호 추가

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])
# def is_child(parent, child):
#     if parent[1] > child[1]:
#         return True
#     return False
# def is_left(parent, child):
#     if parent[0] > child[0]:
#         return True
#     return False
# def get_distance(node1, node2):
#     return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])
# def get_bst(nodeinfo): # nodeinfo[i] = (x, y)
#     root = max(nodeinfo, key=lambda x:x[1])
#     root_index = nodeinfo.index(root)
    
#     bst = [[None, None] for _ in range(len(nodeinfo))]
#     for i in range(0, len(nodeinfo)):
#         if i == root_index:
#             continue
#         node = nodeinfo[i]
#         min_distance = get_distance(node, root)
#         parent_index = root_index
#         for j in range(0, len(nodeinfo)):
#             if i == j:
#                 continue
#             possible_parent = nodeinfo[j]
#             if is_child(possible_parent, node):
#                 distance = get_distance(node, possible_parent)
#                 if min_distance > distance:
#                     min_distance = distance
#                     parent_index = j
#         if is_left(nodeinfo[parent_index], node):
#             bst[parent_index][0] = i
#         else:
#             bst[parent_index][1] = i
#     return bst

# def preorder(root, visited):
#     global BST
#     left_index, right_index = BST[root]
    
#     visited.append(root)
#     if left_index:
#         preorder(left_index, visited)
#     if right_index:
#         preorder(right_index, visited)
# def postorder(root, visitied):
#     global BST
#     left_index, right_index = BST[root]
    
#     if left_index:
#         postorder(left_index, visitied)
#     if right_index:
#         postorder(right_index, visitied)
#     visitied.append(root)

# def solution(nodeinfo):
#     global BST
#     BST = get_bst(nodeinfo)
#     preorder_result = []
#     postorder_result = []
    
#     preorder(0, preorder_result)
#     postorder(0, postorder_result)
#     print(BST)
#     return [preorder_result, postorder_result]
