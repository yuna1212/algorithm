"""
시작 시간: 2022년 5월 31일 오후 9시 50분
소요 시간: 50분
풀이 방법:
    재귀 대신 stack과 반복문으로 구현
"""
ZERO = 0
ONE = 1
MIXED = -1
def get_area_kind(arr, start, size):
    kind = arr[start[0]][start[1]]
    for row in range(start[0], start[0]+size):
        for column in range(start[1], start[1]+size):
            if arr[row][column] != kind:
                return MIXED
    return kind
def get_quadric_pieces(start, size):
    size //=2
    ret = []
    for i in range(2):
        row = start[0] + i*size
        for j in range(2):
            column = start[1] + j*size
            ret.append(((row, column), size))
    return ret
            
def solution(arr):
    stack = [((0, 0), len(arr))]
    counter_of = [0, 0]
    
    while stack:
        start, size = stack.pop()
        area_kind = get_area_kind(arr, start, size)
        if area_kind == MIXED:
            stack += get_quadric_pieces(start, size)
        else:
            counter_of[area_kind] += 1
    
    return counter_of

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))