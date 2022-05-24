"""
시작 시간: 2022년 5월 24일 오후 2시
소요 시간: 3시간
풀이 방법:
    B트리랑 비슷하다
    Tree 구조를 사용하지 않을 수도 있지만,
    고정적인 구조에 반복적으로 값을 탐색하기 때문에 Good
"""
INF = 200001
def fill_nodes(node_id, range_start, range_end):
    global TREE
    if range_start == range_end:
        TREE[node_id] = (H[range_start], H[range_start])
        return
    mid = (range_start + range_end) // 2
    fill_nodes(2*(node_id+1)-1, range_start, mid)
    fill_nodes(2*(node_id+1), mid+1, range_end)
    max_h = max(TREE[2*(node_id+1)-1][0], TREE[2*(node_id+1)][0])
    min_h = min(TREE[2*(node_id+1)-1][1], TREE[2*(node_id+1)][1])
    TREE[node_id] = (max_h, min_h)

def get_h(node_id, node_range_start, node_range_end, target_range_start, target_range_end):
    global TREE
    if node_range_start > target_range_end or node_range_end < target_range_start:
        return -1, INF # 목표구간의 밖의 노드인 경우, 나올 수 없는 값 return
    if target_range_start <= node_range_start  and target_range_end >= node_range_end:
        return TREE[node_id][0], TREE[node_id][1] # 현재 값 리턴
    mid = (node_range_start+node_range_end) // 2
    left = get_h(2*(node_id+1)-1, node_range_start, mid, target_range_start, target_range_end)
    right = get_h(2*(node_id+1), mid+1, node_range_end, target_range_start, target_range_end)
    return max(left[0], right[0]), min(left[1], right[1])
    
for _ in range(int(input())):
    N, Q = map(int, input().split()) # 표지판의 수, 등산로의 수
    H = list(map(int, input().split())) # 해발고도 [100, 130, 120, , ...]
    TREE = [None] * (4*N) # 각 원소는 특정 구간에서의 최대, 최소 해발고도. (최대해발고도, 최소해발고도)
    fill_nodes(0, 0, N-1)
    
    for _ in range(Q):
        a, b = map(int, input().split())
        max_h, min_h = get_h(0, 0, N-1, a, b)
        print(">> ", max_h - min_h)
        


    
    
    