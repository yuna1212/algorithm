"""
시작 시간: 2022년 2월 19일 오후 9시 10분
소요 시간: 1시간 30분
풀이 방법:
    전역변수에 최대 높이를 저장하는 방식으로 품.
    트리 높이를 구하는 함수를 재귀적으로 호출하여 최대 높이를 업데이트함.
"""
from sys import stdin

def inputWalls():
    walls = []
    for _ in range(int(input())):
        walls.append(list(map(int, stdin.readline().split())))
    return walls

def growTree(root, wall):
    # 루트의 자식들 중 하나에 속한다면
    for child in root.children:
        if growTree(child, wall):
            return True
    # 루트의 자식들에 안속하면서, 루트에는 속한다면
    if isChildOf(wall, root.wall):
        root.children.append(TreeNode(wall))
        return True
    # 그것도 아니라면
    return False

def isChildOf(smaller, bigger):
    distance = ((bigger[0]-smaller[0])**2 + (bigger[1]-smaller[1])**2)**0.5
    if distance + smaller[2] < bigger[2]:
        return True
    else:
        return False

class TreeNode:
    def __init__(self, wall):
        self.wall = wall
        self.children = []
       
global maxHeightSum
maxHeightSum = -1
def height(node):
    global maxHeightSum
    if not node.children:
        return 0
    childrenHeights = []
    for child in node.children:
        childrenHeights.append(height(child)+1)
    childrenHeights.sort(reverse=True)
    heightSum = childrenHeights[0] + childrenHeights[1] if len(childrenHeights) > 1 else childrenHeights[0]
    if heightSum > maxHeightSum:
        maxHeightSum = heightSum
    return childrenHeights[0]


def solution():
    walls = inputWalls()
    tree = TreeNode(walls.pop(0))
    for wall in walls:
        growTree(tree, wall)
    return height(tree)
for _ in range(int(input())):
    maxHeightSum = -1
    solution()
    print(">> ",maxHeightSum)