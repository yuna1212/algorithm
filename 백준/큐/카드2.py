"""
시작 시간: 2022-11-26 11:23 PM
소요 시간: 10분
풀이 방법:
"""
from collections import deque
n = int(input())
queue = deque([i for i in range(1, n+1)])
number = 1
i = 0
while queue:
    number = queue.popleft()
    if i%2 == 1:
        queue.append(number)
    i += 1
print(number)
