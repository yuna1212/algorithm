"""
시작 시간: 2022년 3월 11일 오후 8시 15분
소요 시간: 10분
풀이 방법:
    힙 모듈 임포트해서 씀
"""
import heapq
from sys import stdin

N = int(input())
HEAP = []
for _ in range(N):
    x = int(stdin.readline())
    if x > 0:
        heapq.heappush(HEAP, -x)
    else:
        if HEAP:
            print(">> ", -heapq.heappop(HEAP))
        else:
            print(">> ", 0)