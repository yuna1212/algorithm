"""
시작 시간: 2022년 4월 21일 오후 2시 20분
소요 시간: 20분
풀이 방법:
    연결된 노드들을 저장하고, 1번 노드부터 확인해서 누가 부모인지 확인함
    부모는 하나니까
"""
from sys import stdin
n = int(input())
connected = [[] for _ in range(n+1)]
parent_of = [0 for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, stdin.readline().split())
    connected[x].append(y)
    connected[y].append(x)
stack = [1]

while stack:
    parent = stack.pop()
    for child in connected[parent]:
        if parent_of[child] == 0:
            parent_of[child] = parent
            stack.append(child)
 
for s in parent_of[2:]:
    print(s)