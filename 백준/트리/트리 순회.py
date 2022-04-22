"""
시작 시간: 2022년 4월 22일 오후 3시 25분
소요 시간: 30분
풀이 방법:
    Node 클래스 만들어서 preorder, inorder, postorder 차례로 구현
    입력 받을 때 자식 객체 제대로 가리키기위해 리스트에 저장하고, get_node_index 메소드로 알파벳을 통해 리스트에 접근할 인덱스 구하게 함
"""
from sys import stdin

class Node:
    def __init__(self, alpha=None):
        self.alpha = alpha
        self.left, self.right = None, None
    def get_alpha(self):
        return self.alpha
    def set_alpha(self, alpha):
        self.alpha = alpha
    def set_left(self, left):
        self.left = left
    def set_right(self, right):
        self.right = right
    def get_right(self):
        return self.right
    def get_left(self):
        return self.left
    def __repr__(self) -> str:
        return self.alpha
def get_node_index(alpha):
    return ord(alpha) - ord('A')
def make_tree():
    n = int(input())
    nodes = [Node() for _ in range(n)]
    for _ in range(n):
        parent_alpha, left_alpha, right_alpha = stdin.readline().split()
        parent = nodes[get_node_index(parent_alpha)]
        parent.set_alpha(parent_alpha)
        if left_alpha != '.':
            parent.set_left(nodes[get_node_index(left_alpha)])
        if right_alpha != '.':
            parent.set_right(nodes[get_node_index(right_alpha)])
    return nodes
def visit_preorder(tree, root_alpha):
    root = tree[get_node_index(root_alpha)]
    print(root, end="")
    if root.get_left():
        visit_preorder(tree, root.get_left().get_alpha())
    if root.get_right():
        visit_preorder(tree, root.get_right().get_alpha())
def visit_inorder(tree, root_alpha):
    root = tree[get_node_index(root_alpha)]
    if root.get_left():
        visit_inorder(tree, root.get_left().get_alpha())
    print(root, end="")
    if root.get_right():
        visit_inorder(tree, root.get_right().get_alpha())
def visit_postorder(tree, root_alpha):
    root = tree[get_node_index(root_alpha)]
    if root.get_left():
        visit_postorder(tree, root.get_left().get_alpha())
    if root.get_right():
        visit_postorder(tree, root.get_right().get_alpha())
    print(root, end="")

tree = make_tree()
visit_preorder(tree, 'A')
print()
visit_inorder(tree, 'A')
print()
visit_postorder(tree, 'A')