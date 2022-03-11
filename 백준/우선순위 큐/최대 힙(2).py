"""
시작 시간: 2022년 3월 11일 오후 8시 15분
소요 시간: 2시간
풀이 방법:
    - 힙 직접 구현
    - add 메소드에서 while 조건으로 here>0안넣어줘서 계속 실패
    - 이조건 안넣어주면 의도치않은 결과 초래
    - here가 0이 되었을 때, parent는 -1이되고 인덱스로는 배열의 마지막 원소를 참조
"""
from sys import stdin
N = int(input())
HEAP2 = []

def add(element):
    global HEAP2
    HEAP2.append(element)
    if len(HEAP2) > 1:
        here = len(HEAP2) - 1
        parent = (here-1) // 2
        while here > 0 and HEAP2[here] > HEAP2[parent]:
            HEAP2[here], HEAP2[parent] = HEAP2[parent], HEAP2[here]
            here = parent
            parent = (here-1) // 2

def print_max():
    global HEAP2
    if HEAP2:
        # 가장 큰 수 프린트하고 삭제
        print(HEAP2[0])
        HEAP2[0] = HEAP2[-1]
        HEAP2.pop()
        
        here = 0
        while True:
            left = 2*here + 1
            right =2*here + 2
            
            if left >= len(HEAP2):
                # 왼쪽 자식이 리스트 밖에 위치한다면
                break
            next = here
            if HEAP2[next] < HEAP2[left]:
                # 왼쪽 자식보다 작다면, 우선 왼쪽 값과 바꿔야함
                next = left
            if right < len(HEAP2) and HEAP2[next] < HEAP2[right]:
                # 오른쪽 자식이 리스트 안에 위치하고, 바꿀 값이 오른쪽 값보다도 작으면, 우선 오른쪽 값과 다시 바꿔야함
                next = right
            if next == here:
                # 왼쪽 또는 오른쪽 자식과 바꾸지 않는다면 반복 종료
                break
            HEAP2[here], HEAP2[next] = HEAP2[next], HEAP2[here] # 위치 바꾸기
            here = next
    else:
        print(0)
for _ in range(N):
    x = int(stdin.readline())
    if x > 0:
        add(x)
    else:
        print_max()