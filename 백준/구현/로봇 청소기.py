"""
시작 시간: 2022년 4월 21일 오후 12시
소요 시간: 1시간 50분
풀이 방법:
    지문이해하는게 40분보다 더걸렸다
    특히 2-b에 조건이 너무 많이 걸려서 이해하는게 어려웠다.
    
    문장의 조건만 보지말고 로봇이 어떻게 움직이는지 그리면서 읽었다면 더 쉬웠을 것 같다.
"""
from sys import stdin
CLEAN = 2
DIRTY = 0
WALL = 1
def get_left_position(r, c, d):
    moving = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    return r+moving[d][0], c+moving[d][1]
def get_back_position(r, c, d):
    moving = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    return r+moving[d][0], c+moving[d][1]
# 데이터 입력
n, m = map(int, input().split())
r, c, d = map(int, input().split())
area = []
for _ in range(n):
    area.append(list(map(int, stdin.readline().split())))

# 청소 시작
cleaned = 0
repeat = 0
cleaning_completed = False
while not cleaning_completed:
    area[r][c] = CLEAN # 현재 위치 청소
    cleaned += 1
    repeat = 0
    while True:
        left_r, left_c = get_left_position(r, c, d)
        d = (d-1)%4 # 왼쪽 회전
        repeat += 1
        if area[left_r][left_c] == DIRTY: # 왼쪽칸 청소 가능
            r, c = left_r, left_c # 왼쪽칸으로 전진
            break
        else:
            if repeat == 4:
                back_r, back_c = get_back_position(r, c, d)
                if area[back_r][back_c] == WALL:
                    cleaning_completed = True
                    break
                else:
                    r, c = back_r, back_c
                    repeat = 0
print(cleaned)