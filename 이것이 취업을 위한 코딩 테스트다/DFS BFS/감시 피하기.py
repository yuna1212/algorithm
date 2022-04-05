"""
시작 시간: 2022년 4월 5일 오후 3시 40분
소요 시간: 30분
풀이 방법:
    선생님 감시에 닿는 학생이 몇명인지 확인 -> 모든 학생 수에서 빼기
    36C3은 약 7000경우, 따라서 모든 경우의 수 확인해봄
"""
from itertools import combinations
# 입력
n = int(input())
map_info = []
teacher_locations = []
empty_locations = []
student_count = 0
for i in range(n):
    a_line = list(input().split())
    map_info.append(a_line)
    for j in range(n):
        if a_line[j] == "X":
            empty_locations.append((i, j))
        elif a_line[j] == "T":
            teacher_locations.append((i, j))
        else:
            student_count += 1
obstacle_candidates = combinations(empty_locations, 3)

protected_max_student = 0
for obstacles in obstacle_candidates:
    for obstacle in obstacles:
        x, y = obstacle
        map_info[x][y] = "O"
    attacked_student_locations = set()
    for teacher_x, teacher_y in teacher_locations:
        # 상
        x, y = teacher_x-1, teacher_y
        while x >= 0:
            if map_info[x][y] == "O" or map_info[x][y] == "T":
                break
            if map_info[x][y] == "S":
                attacked_student_locations.add((x, y))            
            x -= 1
        # 하
        x, y = teacher_x+1, teacher_y
        while x < n:
            if map_info[x][y] == "O" or map_info[x][y] == "T":
                break
            if map_info[x][y] == "S":
                attacked_student_locations.add((x, y))            
            x += 1
        # 좌
        x, y = teacher_x, teacher_y-1
        while y >= 0:
            if map_info[x][y] == "O" or map_info[x][y] == "T":
                break
            if map_info[x][y] == "S":
                attacked_student_locations.add((x, y))            
            y -= 1
        # 우
        x, y = teacher_x, teacher_y+1
        while y < n:
            if map_info[x][y] == "O" or map_info[x][y] == "T":
                break
            if map_info[x][y] == "S":
                attacked_student_locations.add((x, y))            
            y += 1
    
    protected_max_student = max(protected_max_student, student_count - len(attacked_student_locations))
    
    for obstacle in obstacles:
        x, y = obstacle
        map_info[x][y] = "X"

print("YES") if protected_max_student == student_count else print("NO")