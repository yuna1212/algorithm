"""
시작 시간: 2022년 5월 30일 오후 5시
소요 시간: 1시간
풀이 방법:
    반복문 이용.
    그릴 수 있는 삼각형의 한 변의 길이를 구한 후, 순서대로 숫자를 채워준다.
"""
def get_below_position(position):
    level, order = position
    return level + 1, order
def get_upper_position(position):
    level, order = position
    return level - 1, order - 1
def get_right_position(position):
    level, order = position
    return level, order + 1
def get_arr_index(position):
    level, order = position
    return (level+1)*level//2 + order
def get_triangle_size(n, triangle_ord):
    return n - 3*triangle_ord

def solution(n):
    answer = [0] * (n*(n+1)//2)
    number = 1
    triangle_ord = 0
    position = (0, 0)
    triangle_size = get_triangle_size(n, triangle_ord)
    
    while triangle_size > 0:
        # 아래로
        for _ in range(triangle_size-1):
            answer[get_arr_index(position)] = number
            position = get_below_position(position)
            number += 1
        # 오른쪽으로
        for _ in range(triangle_size-1):
            answer[get_arr_index(position)] = number
            position = get_right_position(position)
            number += 1
        # 위로
        for _ in range(triangle_size-2):
            answer[get_arr_index(position)] = number
            position = get_upper_position(position)
            number += 1
        answer[get_arr_index(position)] = number
        number += 1
        position = get_below_position(position) # 새로운 삼각형의 가장 위 꼭지점 지정
        
        triangle_ord += 1
        triangle_size = get_triangle_size(n, triangle_ord)
    
    return answer
print(solution(4))