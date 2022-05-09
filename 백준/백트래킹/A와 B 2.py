"""
시작 시간: 2022년 5월 9일 오후 6시
소요 시간: 50분
풀이 방법:
    stack에 문자열 계속 넣으면서 탐색
        어차피 목표 길이, 즉 depth가 정해져있다. 
        무조건 정해진 길이의 문자열을 만들어서 확인해야하기 때문에 BFS보다 효율적이다.
    만약 완성된 문자열이 될 수 없다면, 그걸로 문자열을 더 만드는 것 중단
        문자를 추가하는 것만 가능하지, '삭제'를 할 수 는 없기 때문에 이미 T에 포함되어있지 않은 조합에 문자를 추가한다고 정답을 만들 수 없음..
"""
READ_FORWARD = 1
READ_BACKWARD = 2
from sys import stdin
def solution():
    if S not in T:
        if not is_in_T(S):
            print(0)
            return
    stack = [(S, READ_FORWARD)] # 문자열, 읽는 방향
    while stack:
        string, direction = stack.pop()
        if len(string) == len(T): # 완성된 문자열이 T와 같은지 확인
            if resolve(string, direction) == T:
                print(1)
                return
        else: # 문자열 만들어서 넣기
            if not is_in_T(resolve(string, direction)): # 만든 문자열이 앞으로 T가 될 수 없는 문자열이라면
                continue
            stack.append(add_A(string, direction)) # A를 추가한 문자열
            stack.append(add_B(string, direction)) # B를 추가한 문자열
    print(0)
    return
    
def add_A(at_string, direction):
    if direction == READ_FORWARD:
        return at_string + "A", READ_FORWARD
    return "A" + at_string, READ_BACKWARD
def add_B(at_string, direction):
    if direction == READ_FORWARD:
        return at_string+"B", READ_BACKWARD
    return "B"+at_string, READ_FORWARD
def resolve(string, direction):
    if direction == READ_FORWARD:
        return string
    return string[::-1]
def is_in_T(sub_string):
    if sub_string not in T:
        if sub_string[::-1] not in T:
            return False
    return True
# 입력
S = stdin.readline().rstrip()
T = stdin.readline().rstrip()
solution()