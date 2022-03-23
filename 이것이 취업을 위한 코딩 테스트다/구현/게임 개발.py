"""
시작 시간: 2022년 3월 23일 오후 11시 10분
소요 시간: 1시간
풀이 방법:
    반복문이 꼬임,,무한루프
"""
def get_next(now, direction):
    x, y = now
    next = now
    if direction == 0:
        next = x, y-1
    elif direction == 1:
        next = x+1, y
    elif direction == 2:
        next = x, y+1
    else:
        next = x-1, y
    return next

# 입력
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
game_map = []
for _ in range(n):
    row = list(map(int, input().split()))
    game_map.append(row)
game_map[x][y] += 2 # 0이면 방문x, 1이면 바다, 2이면 방문
counter = 0

while True:
    i = 0
    while i < 5: # 모든 방향 확인?
        i += 1
        direction = (direction-1)%4 # 왼쪽 회전
        next_x, next_y = get_next((x, y), direction) # 왼쪽편에 마주보고있는 칸
        
        if game_map[next_x][next_y] > 0: # 다음 칸이 방문된 또는 바다
            continue
            
        # 바라보는 칸으로 한 칸 이동
        x, y = next_x, next_y
        counter += 1
        break
    if i == 4:
        opposite_direction = (direction+2)%4 # 반대 방향
        opposite_next_x, opposite_next_y = get_next((x, y), opposite_direction)
        if game_map[opposite_next_x][opposite_next_y] == 1:
            # 반대 방향이 바다라면
            break
        # 방향 유지하고 한 칸 뒤로
        x, y = opposite_next_x, opposite_next_y
        counter += 1
print(counter)