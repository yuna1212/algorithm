"""
시작 시간: 2022-11-15 11:52 PM
소요 시간: 50분
풀이 방법:
"""
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
MOVABLE, UNMOVABLE = 0, 1
def get_left(x, y, direction):
    """ 현재 위치, 방향 기준 왼쪽 칸 위치 구하기 """
    if direction == WEST:
        return x+1, y
    elif direction == EAST:
        return x-1, y
    elif direction == SOUTH:
        return x, y+1
    elif direction == NORTH:
        return x, y-1
    return nx, ny

def get_back(x, y, direction):
    """ 현재 위치, 방향 기준 왼쪽 칸 위치 구하기 """
    if direction == WEST:
        return x, y+1
    elif direction == EAST:
        return x, y-1
    elif direction == SOUTH:
        return x-1, y
    elif direction == NORTH:
        return x+1, y

def solution(grid, x, y, direction):
    ret = 0
    while True:
        moved = False
        # 현재 위치로 움직였다고 기록
        ret += 1
        grid[x][y] = UNMOVABLE
        for turning_count in range(4):
            # 왼쪽 방향으로 돌기
            nx, ny = get_left(x, y, direction)
            direction = (direction- 1) % 4
            if grid[nx][ny] == UNMOVABLE:
                # 왼쪽으로 직진할 수 없다면 다시 돌러 가기 
                continue
            else:
                # 왼쪽으로 직진 
                x, y = nx, ny
                moved = True
                break
        # 움직였다면 돌러 가기
        if moved: continue
        # 움직일 수 없었다면 뒤로 이동 
        nx, ny = get_back(x, y, direction)
        if grid[nx][ny] == MOVABLE:
            x, y = nx, ny
        else:
            break
    return ret

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

print(solution(grid, x, y, direction))

