"""
시작 시간: 2023-01-03 09:56 PM
소요 시간: 40분
풀이 방법:
"""
from collections import deque

n, w, l = map(int, input().split()) # 트럭 수, 다리 길이, 다리 최대 하중
trucks_weights = list(map(int, input().split()))

bridge_weight = 0
now_time = 0
on_bridge = deque()

for truck_weight in trucks_weights:
    bridge_weight += truck_weight
    now_time += 1

    while bridge_weight > l:
        # 다리 하중을 초과한다면, 초과하지 않을 때 까지 트럭을 빼야 한다.
        head_weight, entered_time = on_bridge.popleft()
        bridge_weight -= head_weight
        moving_time = now_time - entered_time

        if moving_time < w: 
            # 가장 앞의 트럭이 아직 다리 위에 있는 경우
            # 다리를 빠져나갈 때 까지 기다린다.
            now_time = entered_time + w

    on_bridge.append((truck_weight, now_time))

now_time = on_bridge[-1][1] + w
print(now_time)

