"""
시작 시간: 2022년 4월 25일 오후 2시 45분
소요 시간: 1시간
풀이 방법:
    풀이는 비슷한데 무한루프,,값 범위를 잘못 설정하게 함
"""
from sys import stdin

def postorder_print(start, end):
    global PREORDER
    if end <= start:
        return
    left_idx, right_idx = start + 1, start
    for i in range(start, end+1):
        if PREORDER[start] < PREORDER[i]:
            right_idx = i
            break
    postorder_print(left_idx, right_idx)
    postorder_print(right_idx, end)
    print(PREORDER[start])
    

PREORDER = []
while True:
    try:
        num = int(stdin.readline())
        PREORDER.append(num)
    except:
        break
if PREORDER:
    postorder_print(0, len(PREORDER)-1)
