"""
시작 시간: 2022년 3월 20일 오전 12시
소요 시간: 15분
풀이 방법:
    input() 메소드때문에 시간 오래걸림 -> sys.stdin.readline으로 바꿔서 해결
"""
import heapq
from sys import stdin
N = int(input())
heap = []
for _ in range(N):
    x = int(stdin.readline())
    if x > 0:
        heapq.heappush(heap, x)
    elif heap:
        print(heapq.heappop(heap))
    else:
        print(0)