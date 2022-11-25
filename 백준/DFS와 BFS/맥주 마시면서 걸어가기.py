"""
시작 시간: 2022-11-25 01:46 PM
소요 시간: 1시간
풀이 방법: 거리는 단방향으로 딱 한번밖에 사용하지 않으므로 미리 계산해서 저장해두는 것 보다 매번 계산하는게 효율적이다
"""
import sys
from collections import deque
input = sys.stdin.readline
MAX_DISTANCE = 20*50

def get_distance(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def is_reachable(positions):
    visited = set()
    queue = deque([0]) # position 인덱스
    while queue:
        now= queue.popleft()
        if now in visited:
            continue
        visited.add(now)
        if now == len(positions) - 1:
            return True
        for i in range(len(positions)):
            distance = get_distance(positions[now], positions[i])
            if distance <= MAX_DISTANCE:
                queue.append(i) 
    return False
    
def solution():
    n = int(input().strip())
    positions = [] # positions[0]에서 출발해서 positions[n-1]로 갈 수 있는지
    for _ in range(n+2):
        positions.append(tuple(map(int, input().strip().split())))
    if is_reachable(positions):
        print("happy")
    else:
        print("sad")

for _ in range(int(input().strip())):
    solution()
