"""
시작 시간: 2022년 2월 18일 오후 9시 50분
소요 시간: 15분
풀이 방법:
    수열이 저장된 리스트의 인덱스를 스택에서 다룸.
    프로그래머스 주식가격 문제와 유사하다.
"""
input()
numbers = list(map(int, input().split()))
stack = []
nge = [-1]*len(numbers)
for i in range(len(numbers)):
    while stack and numbers[stack[-1]] < numbers[i]:
        nge[stack.pop(-1)] = numbers[i]
    stack.append(i)

for number in nge:
    print(number, end=" ")