"""
시작 시간: 2023-02-02 01:57 PM
소요 시간: 20분
풀이 방법: dfs인데 맵에 직접 표시 안하고 visited에 표시했으면 더 좋았을 듯
"""
def get_map_array_style(map):
    array_style_map = []

    for line in map:
        new_line = []

        for char in line:
            if char != 'X':
                char = int(char)
            new_line.append(char)

        array_style_map.append(new_line)

    return array_style_map

def is_valid_position(x, y):
    global MAP

    if not (0 <= x < len(MAP) and 0 <= y < len(MAP[0])):
        return False

    return True

def dfs(x, y):
    global MAP
    food = 0
    stack = [(x, y)]
    diffs = ((-1, 0), (1, 0), (0, 1), (0, -1))
    while stack:
        x, y = stack.pop()

        if not is_valid_position(x, y):
            continue

        if MAP[x][y] == 'X':
            continue
        
        food += MAP[x][y]
        MAP[x][y] = 'X'

        for dx, dy in diffs:
            stack.append((x+dx, y+dy))

    return food

def solution(maps):
    global MAP
    MAP = get_map_array_style(maps) 
    answer = []
    for i in range(len(MAP)):
        for j in range(len(MAP[0])):
            food = dfs(i, j)
            if food > 0:
                answer.append(food)

    if len(answer) == 0:
        return [-1]

    answer.sort()
    return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
