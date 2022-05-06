"""
시작 시간: 2022년 5월 6일 오후 3시 30분
소요 시간: 1시간
풀이 방법:
    문제를 잘못 이해했다. 대기실에서 규칙 어긴 사람이 몇명인지 세는건줄 알았다..
    BFS로 금방 풀 수 있었는데 괜히 다익스트라인지 플로이드 워셜로 풀어야할지 고민했다.
"""
from collections import deque
INF = 30
ROOM_SIZE = 5
def solution(places):
    valid_info = [0] * 5
    for i, place in enumerate(places):
        if is_valid_place(place):
            valid_info[i] = 1
    return valid_info

def is_valid_place(place):
    for x in range(ROOM_SIZE):
        for y in range(ROOM_SIZE):
            if place[x][y] == "P":
                if not is_valid_person(place, x, y):
                    return False
    return True
    
def is_valid_person(place, x, y):
    visitied = [[False]*ROOM_SIZE for _ in range(ROOM_SIZE)] 
    queue = deque([(0, x, y)])
    diff = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        distance, x, y = queue.popleft()
        if visitied[x][y]:
            continue
        if place[x][y] == "P":
            if 0 < distance <= 2:
                return False
        visitied[x][y] = True
        distance += 1
        for dx, dy in diff:
            nx, ny = x+dx, y+dy
            if 0<= nx < ROOM_SIZE and 0<= ny < ROOM_SIZE:
                if place[nx][ny] != "X":
                    queue.append((distance, nx, ny))
    return True
    
a= solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
print(a)