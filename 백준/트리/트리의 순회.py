"""
시작 시간: 2023-02-10 11:09 AM
소요 시간: 2시간 40분
풀이 방법: 똑같은 풀이에 recursion limit 설정 안해줘서 recursion error, 메모리 초과 판정됨 
"""
import sys
sys.setrecursionlimit(10**5)
START_IDX = 0
END_IDX = 1
def print_preorder(postorder_range, inorder_range):
    if postorder_range[START_IDX] > postorder_range[END_IDX]:
        return

    middle_value = postorder[postorder_range[END_IDX]]
    inorder_middle_idx = -1
    for i in range(inorder_range[START_IDX], inorder_range[END_IDX]+1):
        if inorder[i] == middle_value:
            inorder_middle_idx = i
            break
    
    left_tree_size = inorder_middle_idx - inorder_range[START_IDX]
    postorder_middle_idx = postorder_range[START_IDX] + left_tree_size

    print(middle_value, end=" ")
    
    # 왼쪽 트리 방문
    print_preorder([postorder_range[START_IDX], postorder_middle_idx-1],\
                   [inorder_range[START_IDX], inorder_middle_idx - 1])
    
    # 오른쪽 트리 방문
    print_preorder([postorder_middle_idx, postorder_range[END_IDX] - 1],\
                   [inorder_middle_idx+1, inorder_range[END_IDX]])

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

print_preorder([0, n-1], [0, n-1])
