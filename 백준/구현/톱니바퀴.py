"""
시작 시간: 2022-11-28 10:08 PM
소요 시간: 1시간 20분
풀이 방법: 너무 복잡한 상수 쓰니까 코드 작성하면서 나도 헷갈리고 가독성 떨어져서 디버깅하기도 힘들다..
"""

WHEELS = [None]
RIGHT, LEFT = 0, 1
SAWTOOTH_IDX_DIRECTION_OF = [6, 2]
CLOCKWISE, COUNTERCLOCKWISE =   1, -1

def turn_clockwise(wheel_idx):
    sawtooth = WHEELS[wheel_idx]
    tmp = sawtooth[-1]
    for i in range(len(sawtooth)-1, 0, -1):
        sawtooth[i] = sawtooth[i-1]
    sawtooth[0] = tmp

def turn_counterclockwise(wheel_idx):
    sawtooth = WHEELS[wheel_idx]
    tmp = sawtooth[0]
    for i in range(1, len(sawtooth)):
        sawtooth[i-1] = sawtooth[i]
    sawtooth[-1] = tmp


def turn(wheel_idx, turning_direction, spreading_direction):
    sawtooth = WHEELS[wheel_idx]
    adjacent_value = sawtooth[SAWTOOTH_IDX_DIRECTION_OF[(spreading_direction+1)%2]] # 다음 바퀴와 맞닿은 현재 바퀴의 톱니 값 저장

    # 해당 바퀴 회전
    if turning_direction == CLOCKWISE:
        turn_clockwise(wheel_idx)
    else:
        turn_counterclockwise(wheel_idx)

    next_wheel_idx = wheel_idx - 1 if spreading_direction == LEFT else wheel_idx + 1
    if next_wheel_idx <= 0 or next_wheel_idx >= len(WHEELS): return

    next_adjacent_value = WHEELS[next_wheel_idx][SAWTOOTH_IDX_DIRECTION_OF[spreading_direction]] # 다음 바퀴의 맞닿은 톱니 저장
    if adjacent_value == next_adjacent_value: return

    turn(next_wheel_idx, -1*turning_direction, spreading_direction) # 다음 바퀴 회전시키러

for _ in range(4):
    WHEELS.append(list(input()))

for _ in range(int(input())):
    wheel_idx, turning_direction = map(int, input().split())
    turn(wheel_idx, turning_direction, RIGHT)
    if turning_direction == CLOCKWISE:
        turn_counterclockwise(wheel_idx)
    else:
        turn_clockwise(wheel_idx)
    turn(wheel_idx, turning_direction, LEFT)

scores = [0, 1, 2, 4, 8]
ans = 0
for i in range(1, len(WHEELS)):
    ans += int(WHEELS[i][0])*scores[i]
print(ans)
