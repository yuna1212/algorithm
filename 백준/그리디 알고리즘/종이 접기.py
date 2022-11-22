"""
시작 시간: 2022-11-22 03:34 PM
소요 시간: 3시간 30분
풀이 방법: 이진 탐색을 같은 레벨끼리 묶어서 처리 -> BFS
"""
import sys
from collections import deque
input = sys.stdin.readline

def solution(bits):
    l = (len(bits) - 1)//2
    cycle = 0
    queue = deque([l])
    count = 2**cycle
    l = (l - 1)//2
    last_bit = -1
    while queue:
        index = queue.popleft()
        if index < 0 or index >= len(bits): continue
        if last_bit == bits[index]:
            return False
        last_bit = bits[index]
        if l < 0: continue
        queue.append(index - l - 1)
        queue.append(index + l + 1)
        count -= 1
        if count == 0:
            last_bit = -1
            l = (l - 1)//2
            cycle += 1
            count = 2**cycle
    return True

t = int(input().strip())
for a in range(t):
    bits = input().strip()
    length = (len(bits) - 1)//2
    if solution(bits):
        print("YES")
    else:
        print("NO")

