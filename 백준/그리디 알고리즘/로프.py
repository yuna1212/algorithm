"""
시작 시간: 2022-10-18 04:47 PM
소요 시간: 20분
풀이 방법:
    - 완탐 필수. 중간에 최적해라고 확신할 수 없다. ex) 가장작은로프=8, k=9 -> 가장작은로프=7, k=11
"""
import sys
import heapq
input = sys.stdin.readline
k = int(input())
lopes = []
for _ in range(k):
    heapq.heappush(lopes, -int(input().strip()))
k = 1
ans = - heapq.heappop(lopes)
while lopes:
    lope = heapq.heappop(lopes)
    k += 1
    avg_weight = - lope*k
    ans = max(avg_weight, ans)
print(ans)
