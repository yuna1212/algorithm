"""
시작 시간: 2022년 2월 5일 오후 6시 50분
소요 시간: 1시간
풀이 방법:
    스택 적절히 구현
"""
stack = []
sequencialNumber = 1
operators = []
for _ in range(int(input())):
    element = int(input())
    while sequencialNumber <= element:
        stack.append(sequencialNumber)
        operators.append("+")
        sequencialNumber += 1

    # 이제 스택에 넣을 숫자는 원소보다 큰 수
    # 스택에 넣어진 최대 수는 원소 이하임
    if stack:
        popped = stack.pop()
        operators.append("-")
    else:
        # 조건에 맞는 수까지 스택을 채웠음에도 스택이 비어있는 경우, 수열을 만들어낼 수 없음
        print("NO")
        operators = None
        break

    # 빈 스택이 아닐 경우, 스택에서 하나씩 꺼냄
    while stack and popped > element:
        popped = stack.pop()
        operators.append("-")

    # 마지막에 꺼낸 수가 원소보다 작은 경우, 주어진 수열을 만들 수 없음
    if popped < element:
        print("NO")
        operators = None
        break

if operators:
    for operator in operators:
        print(operator)