"""
시작 시간: 2022-11-22 12:57 PM
소요 시간: 1시간 50분
풀이 방법: O(N^2logN) 풀이 -> 시간초과, 블로그 풀이 참고: O(NlogN)
"""
import sys, heapq
input = sys.stdin.readline
"""
n = int(input().strip())

deadline_cupramens = []
for _ in range(n):
    deadline, cupramen = map(int, input().strip().split())
    heapq.heappush(deadline_cupramens, (-deadline, cupramen))

ans = 0
last_deadline = -1
max_cupramen = 0
while deadline_cupramens:
    deadline, cupramen = heapq.heappop(deadline_cupramens)
    deadline = -deadline

    if deadline <= 0: 
        break

    if deadline != last_deadline:
        ans += max_cupramen
        if ans >= 2**31: break
        last_deadline = deadline
        max_cupramen = cupramen
        continue

    if max_cupramen < cupramen:
        heapq.heappush(deadline_cupramens, (-deadline+1, max_cupramen))
        max_cupramen = cupramen

    else:
        heapq.heappush(deadline_cupramens, (-deadline+1, cupramen))

ans += max_cupramen
if ans >= 2**31:
    print(2**31)
else:
    print(ans)
"""
n = int(input().strip())
deadline_cupramens = []
for _ in range(n):
    deadline_cupramens.append(tuple(map(int, input().strip().split())))
deadline_cupramens.sort(key = lambda x: (x[0], -x[1]))

heap = []
for deadline, cupramen in deadline_cupramens:
    heapq.heappush(heap, cupramen)
    if deadline < len(heap):
        heapq.heappop(heap)
print(sum(heap))
