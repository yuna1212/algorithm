"""
시작 시간: 2023-01-04 11:37 PM
소요 시간: 1시간 10분
풀이 방법: 무한루프,,
"""
def get_connection(x, y, is_visited):
    global MAP, WIDTH, HEIGHT
    color = MAP[x][y]
    connection = []
    stack = [ (x, y) ]
    diffs = ((-1, 0), (1, 0), (0, 1), (0, -1))
    while stack:
        x, y = stack.pop()
        if not (0 <= x < HEIGHT) or not (0 <= y < WIDTH) or is_visited[x][y] or color != MAP[x][y]:
            continue

        for dx, dy in diffs:
            nx, ny = x + dx, y + dy
            stack.append((nx, ny))

        is_visited[x][y] = True
        connection.append((x, y))
    return connection
        
def explode(bombs):
    global MAP, BLK
    for bomb in bombs:
        for x, y in bomb:
            MAP[x][y] = BLK 

def set_gravity():
    global MAP, WIDTH, HEIGHT
    puyo_heights = [HEIGHT-1] * WIDTH

    for x in range(HEIGHT - 1, -1, -1):
        for y in range(WIDTH):
            if MAP[x][y] == BLK:
                while puyo_heights[y] >= 0 and puyo_heights[y] == BLK:
                    puyo_heights[y] -= 1
                MAP[x][y] = MAP[puyo_heights[y]][y]
                MAP[puyo_heights[y]][y] = BLK 

            puyo_heights[y] -= 1


BLK = '.'
WIDTH = 6
HEIGHT = 12
MAP = []
for _ in range(HEIGHT):
    MAP.append(list(input()))

ans = 0

while True:
    is_visited = [[False]*WIDTH for _ in range(HEIGHT)]
    bombs = []
    for x in range(HEIGHT - 1, -1, -1):
        for y in range(0, WIDTH):
            bomb = get_connection(x, y, is_visited)
            if len(bomb) < 4:
                continue
            bombs.append(bomb)

    if len(bombs) < 0:
        break

    explode(bombs)
    set_gravity()
    ans += 1

print(ans)


