"""
시작 시간: 2022년 3월 20일 오전 1시
소요 시간: 40분
풀이 방법:
    힙에 값 2개(절댓값, 원본값)씩 저장
"""
import heapq
from sys import stdin
N = int(input())
heap = []
for _ in range(N):
    x = int(stdin.readline())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if not heap:
            print(0)
            continue
        item = heapq.heappop(heap)
        if item[1] < 0:
            print(item[1])
            continue
        push_back = []
        while heap and item[0] == heap[0][0]:
            push_back.append(item)
            item = heapq.heappop(heap)
            if item[1] < 0:
                break
        for i in push_back:
            heapq.heappush(heap, i)
        print(item[1])
