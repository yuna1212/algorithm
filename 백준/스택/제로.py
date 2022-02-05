"""
시작 시간: 2022년 2월 5일 오후 4시 50분
소요 시간: 5분
풀이 방법:
    스택 구현.
"""
stack = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))