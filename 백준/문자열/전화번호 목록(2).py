"""
시작 시간: 2022-10-19 04:21 PM
소요 시간: 50분
풀이 방법: Trie로 풀이. 정렬은 필요 없다!
"""
import sys
input = sys.stdin.readline
class Node:
    def __init__(self, is_end):
        self.is_end = is_end
        self.children = dict()

    def get_next(self, number):
        if number not in self.children:
            self.children[number] = Node(False)
        return self.children[number]

def is_consistent(phones):
    root = Node(False)
    for numbers in phones:
        node = root
        for number in numbers:
            node = node.get_next(number)
            if node.is_end: 
                return False
        if len(node.children) > 0:
            return False
        node.is_end = True
    return True
     
for _ in range(int(input().strip())):
    phones = []
    for _ in range(int(input().strip())):
        phones.append(input().strip())
    if is_consistent(phones):
        print("YES")
    else:
        print("NO")

