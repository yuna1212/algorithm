"""
시작 시간: 2022년 4월 13일 오후 5시
소요 시간: 30분 
풀이 방법:
    매번 명령어 실행하다보면 시간초과
"""
from sys import stdin
T = int(input())
for _ in range(T):
    # 입력
    p = list(stdin.readline().rstrip())
    n = int(stdin.readline())
    input_arr = stdin.readline().rstrip()
    
    # 알고리즘
    index = 1
    arr = []
    is_err = False
    arr = input_arr[1:-1].split(",")
    if arr[0] == "":
        arr.pop(0)
    for op in p:
        if op == "R":
            arr.reverse()
        else:
            if not arr:
                is_err = True
                break
            arr.pop(0)
    if is_err:
        print("error")
    else:
        if arr:
            print("[", end="")
            for i in range(len(arr)-1):
                print(arr[i]+",", end="")
            print(arr[-1]+"]")
        else:
            print("[]")