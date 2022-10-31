"""
시작 시간: 2022-10-31 11:34 PM
소요 시간: 3시간
풀이 방법:
    - O(N^2)로 풀이
    - N이 1000일 때(1M) 부분성공
    - N이 100000일 때(10G) 실패
    - 여러 개의 기프티콘의 기한, 계획이 같을 때 처리를 못해서 푸는데 시간 오래걸림
"""
import sys
import math
import heapq
input = sys.stdin.readline
n = int(input().strip())
deadlines = []
dues = []
deadlines = list(map(int, input().strip().split()))
for i, due in enumerate(input().strip().split()):
    heapq.heappush(dues, (int(due), i))

ans = 0
while dues:
    extending_count = 0
    due, due_i = heapq.heappop(dues)
    due_indecies = set()
    due_indecies.add(due_i)
    while dues and due == dues[0][0]:
        _, due_i = heapq.heappop(dues)
        due_indecies.add(due_i)
    for due_i in due_indecies:
        if deadlines[due_i] < due:
            extending_count = math.ceil((due - deadlines[due_i]) / 30)
            ans += extending_count
            deadlines[due_i] += 30*extending_count
        for i in range(n):
            if deadlines[i] < 0 or i in due_indecies: continue
            if deadlines[i] < deadlines[due_i]:
                extending_count = math.ceil((deadlines[due_i] - deadlines[i]) / 30)
                ans += extending_count
                deadlines[i] += 30*extending_count
        deadlines[due_i] = -1

print(ans)
