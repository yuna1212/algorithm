"""
시작 시간: 2022-09-03 PM 05:04
소요 시간: 30분 
풀이 방법: 범위 제한, 이미 방문한 곳 제외하는 것에 주의
"""
from collections import deque

N, K = map(int, input().split())
queue = deque([(N, 0)])
visited = set()
while queue:
    now_position, time = queue.popleft()
    if now_position == K:
        print(time)
        break
        continue
    if now_position < 0 or now_position > 100000:
    # 다음 포지션 탐색
    next_positions = [now_position+1, now_position-1, now_position*2]
    next_time = time+1
    for next_position in next_positions:
        if next_position not in visited:
            visited.add(next_position)
            queue.append((next_position, next_time))
