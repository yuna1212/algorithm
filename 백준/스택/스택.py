"""
시작 시간: 2022년 2월 5일 오후 4시 40분
소요 시간: 10분
풀이 방법:
    스택 구현
"""
from sys import stdin
stack = []
for _ in range(int(input())):
    command = list(stdin.readline().split())
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif command[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)