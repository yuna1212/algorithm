"""
시작 시간: 2022년 6월 9일 오전 11시 45분
소요 시간: 1시간
풀이 방법:
    행, 열의 개수 잘못 설정해서 그거 고치느라 시간이 많이 걸렸다..
"""         
def rotate_and_get_min(grid, query):
    x, y = query[0] - 1, query[1] - 1
    width = query[3]-query[1]
    height = query[2]-query[0]
    number = grid[x][y]
    min_number = number
    
    for _ in range(width):
        y += 1
        grid[x][y], number = number, grid[x][y]
        min_number = min(number, min_number)
    
    for _ in range(height):
        x += 1
        grid[x][y], number = number, grid[x][y]
        min_number = min(number, min_number)
    
    for _ in range(width):
        y -= 1
        grid[x][y], number = number, grid[x][y]
        min_number = min(number, min_number)
    
    for _ in range(height):
        x -= 1
        grid[x][y], number = number, grid[x][y]
        min_number = min(number, min_number)

    return min_number
    
def solution(rows, columns, queries):
    answer = []
    grid = []
    
    for i in range(rows):
        line = [i*columns+j+1 for j in range(columns)]
        grid.append(line)
    
    for query in queries:
        answer.append(rotate_and_get_min(grid, query))
        
    return answer
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))