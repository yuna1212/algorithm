"""
시작 시간: 2022년 4월 27일 오후 1시 40분
소요 시간: 2시간
풀이 방법:
    상어가 이동한 후 자리 차지하면서, 그 자리에 있던 상어 없어지는 것 반영 못함
    같은 시간동안 움직였던 상어가 다시 움직이게 되면서 문제 발생
"""
def printMAP():
    global MAP
    print()
    for line in MAP:
        for fish in line:
            if fish:
                print(fish[2], end = " ")
            else:
                print(0, end=" ")
        print()
    print()
def do_fishing(c):
    global MAP, R
    fish_size = 0
    for r in range(R):
        if MAP[r][c]:
            fish_size = MAP[r][c][2]
            MAP[r][c] = None
            break
    return fish_size
def move_shark(r, c):
    printMAP()
    global MAP, R, C
    s, d, z, time = MAP[r][c]
    MAP[r][c] = None
    if d == 1:
        # 위로 이동
        r -= s
        if r < 0:
            r = -r
            d = 2
            if r >= R:
                r = 2*(R-1) - r
                d = 1
    elif d == 2:
        # 아래로 이동
        r += s
        if r >= R:
            r = 2*(R-1) - r
            d = 1
            if r < 0:
                r = -r
                d = 2
    elif d == 3:
        # 오른쪽으로 이동
        s %= C
        if s > 2*C-c:
            c = s - 2*C-c
        else:
            c += s
            if c >= C:
                c = 2*(C-1) - c
                d = 4
                if c < 0:
                    c = -c
                    d = 3
    elif d == 4:
        # 왼쪽으로 이동
        c -= s
        if c < 0:
            c = -c
            d = 3
            if c >= C:
                c = 2*(C-1) - c
                d = 4
    if MAP[r][c] and MAP[r][c][3] == time:
        MAP[r][c] = max(MAP[r][c], (s, d, z, time+1), key=lambda x: x[2])
    else:
        MAP[r][c] = (s, d, z, time+1)
R, C, M = map(int, input().split())
MAP = [[None for _ in range(C)] for _ in range(R)]
sharks_position = []
fisher = 0
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    if d == 1 or d == 2:
        s %= 2*(R-1)
    else:
        s %= 2*(C-1)
    MAP[r-1][c-1] = (s, d, z, 0) # 속력, 이동방향, 크기
bucket = 0
while fisher < C:
    bucket += do_fishing(fisher)
    sharks = []
    for r in range(R):
        for c in range(C):
            if MAP[r][c]:
                sharks.append((r, c))
    print(sharks)
    for r, c in sharks:
        move_shark(r, c)
    print("낚시꾼 위치는", fisher, "낚시 끝나고 물고기 이동")
    printMAP()
    fisher += 1
print(bucket)
