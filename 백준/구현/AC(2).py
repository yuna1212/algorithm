"""
시작 시간: 2022년 4월 13일 오후 5시 35분
소요 시간: 30분
풀이 방법:
    결국 양 끝에서 알파벳 삭제
    양 끝에서 삭제하는 개수와 reversing 되는 횟수 저장하기
"""
from sys import stdin
def compress_operations(ops):
    count_reversing = 0
    count_pre_popping = 0
    count_post_popping = 0
    for p in ops:
        if p == "R":
            count_reversing += 1
        else:
            if count_reversing%2:
                 # 홀수 -> 1번 뒤집기
                count_post_popping += 1
            else:
                count_pre_popping += 1
    return count_reversing, count_pre_popping, count_post_popping
                
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
    count_reversing, count_pre_popping, count_post_popping = compress_operations(p)
    
    
    if count_pre_popping + count_post_popping > n:
        print("error")
    else:
        if count_post_popping > 0:
            arr = arr[count_pre_popping:-count_post_popping]
        else:
            arr = arr[count_pre_popping:]
        if count_reversing % 2:
            arr.reverse()
        
        if arr:
            print("[", end="")
            for i in range(len(arr)-1):
                print(arr[i]+",", end="")
            print(arr[-1]+"]")
        else:
            print("[]")