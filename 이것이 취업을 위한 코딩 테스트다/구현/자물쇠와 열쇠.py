"""
시작 시간: 2022년 4월 13일 오후 12시 50분
소요 시간: 40분
풀이 방법:
    너무 효율적으로만 풀려고 했다,,
    하지만 배열의 크기가 충분히 작기 때문에, 완전탐색을 해도 무리 없음..
"""
def get_core_area(area, core):
    top, right, left, bottom = 20, 0, 20, 0
    for i in range(len(area)):
        for j in range(len(area)):
            if area[i][j] == core:
                if i < top:
                    top = i
                if i > bottom:
                    bottom = i
                if j < left:
                    left = j
                if j > right:
                    right = j
    core_area = []
    for i in range(top, bottom + 1):
        row = []
        for j in range(left, right+1):
            row.append(area[i][j])
        core_area.append(row)
    return core_area

def rotate(key):
    # 왼쪽으로 90도
    rotated_key = []
    for i in range(len(key[0])-1, -1, -1):
        row = []
        for j in range(len(key)):
            row.append(key[j][i])
        rotated_key.append(row)
    return rotated_key

def is_okay(lock_core, key_core):
    if len(lock_core) != len(key_core):
        return False
    if len(lock_core[0]) != len(key_core[0]):
        return False
    for i in range(len(lock_core)):
        for j in range(len(key_core)):
            if lock_core[i] + lock_core[j] > 1:
                return False
    return True
                

def solution(key, lock):
    key_bump_area, lock_engrave_area = get_core_area(key, 1), get_core_area(lock, 0)
    print(">>>>>>>>>lock")
    for i in range(len(lock_engrave_area)):
        for j in range(len(lock_engrave_area[0])):
            print(lock_engrave_area[i][j], end=" ")
        print()
    
    print(">>>>>>>>>key")
    for i in range(len(key_bump_area)):
        for j in range(len(key_bump_area[0])):
            print(key_bump_area[i][j], end=" ")
        print()
    
    if is_okay(lock_engrave_area, key_bump_area):
        return True
    for _ in range(3):
        key_bump_area = rotate(key_bump_area)
        if is_okay(lock_engrave_area, key_bump_area):
            return True    
    return False
solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])