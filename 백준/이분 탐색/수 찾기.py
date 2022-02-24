"""
시작 시간: 2022년 2월 24일 오전 10시 55분
소요 시간: 50분
풀이 방법:
    클래스로 트리 구현...시간초과
"""
class Node:
    def __init__(self, value, leftNode, rightNode):
        self.value = value
        self.left = leftNode
        self.right = rightNode
        
    def makeTree(self, number):
        if number > self.value:
            if self.right:
                self.right.makeTree(number)            
            else:
                self.right = Node(number, None, None)
        elif number < self.value:
            if self.left:
                self.left.makeTree(number)
            else:
                self.left = Node(number, None, None)
    
    def isSameNumber(self, number):
        if self.value == number:
            return True
        elif self.left and self.value > number:
            return self.left.isSameNumber(number)
        elif self.right and self.value < number:
            return self.right.isSameNumber(number)
        else:
            return False

def inputData():
    input()
    treeNums = list(map(int, input().split()))
    input()
    targets = list(map(int, input().split()))
    return treeNums, targets

def makeTree(treeNums):
    tree = Node(treeNums[0], None, None)
    for i in range(1, len(treeNums)):
        tree.makeTree(treeNums[i])
    return tree

def showExisting(tree, targets):
    for target in targets:
        if tree.isSameNumber(target):
            print(1)
        else:
            print(0)

def solution():
    treeNums, targets = inputData()
    tree = makeTree(treeNums)
    showExisting(tree, targets)

solution()