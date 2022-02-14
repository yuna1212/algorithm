"""
시작 시간: 2022년 2월 14일 오전 8시 50분
소요 시간: 30분
풀이 방법:
    책에 나온 전략대로 구현.
    루트 노드만 출력하고, 순서대로 왼쪽 서브트리, 오른쪽 서브트리를 재귀호출로 탐색한다.
    왼쪽 서브트리와 오른쪽 서브트리는 전위순회와 중위순회 결과로 도출할 수 있다.
"""
from sys import stdin


def printPostOrder(preorder, inorder):
    if not preorder:
        return
    root = preorder[0]
    leftTreeSize = inorder.index(root)
    # 왼쪽
    printPostOrder(preorder[1:1+leftTreeSize], inorder[:leftTreeSize])
    # 오른쪽
    printPostOrder(preorder[leftTreeSize+1:], inorder[leftTreeSize+1:])
    print(root, end=" ")
for _ in range(int(input())):
    input()
    preorder = list(map(int, stdin.readline().split()))
    inorder = list(map(int, stdin.readline().split()))
    printPostOrder(preorder, inorder)
    