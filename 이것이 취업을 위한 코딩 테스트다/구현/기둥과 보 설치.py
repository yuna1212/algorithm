"""
시작 시간: 2022년 4월 13일 오후 1시 45분
소요 시간: 1시간 10분
풀이 방법:
    구현,,,,인데 하다가 변수 꼬이고, 분기식 꼬이고..
"""
PILLAR = 0
FOUNDATION = 1
def is_pillar_possible(x, y, frame):
    if y == 0:
        return True
    if x-1 >= 0 and frame[x-1][y][FOUNDATION]:
        return True
    if frame[x][y][FOUNDATION]:
        return True
    if y-1 >= 0 and frame[x][y-1][PILLAR]:
        return True
    return False

def is_foundation_possible(x, y, frame):
    if y-1 >= 0 and frame[x][y-1][PILLAR]:
        return True
    if x+1<len(frame) and frame[x+1][y-1][PILLAR]:
        return True
    if x-1 >= 0 and x+1<len(frame):
        if frame[x-1][y][FOUNDATION] and frame[x+1][y][FOUNDATION]:
            return True
    return False

def is_pillar_delation_possible(x, y, frame):
    n = len(frame)
    if y+1<n:
        if frame[x][y+1][PILLAR] and not is_pillar_possible(x, y+1, frame):
            return False
        if frame[x][y+1][FOUNDATION] and not is_foundation_possible(x, y+1, frame):
            return False
        if x-1>=0 and frame[x-1][y+1][FOUNDATION] and not is_foundation_possible(x-1, y+1, frame):
            return False
    return True

def is_foundation_delation_possible(x, y, frame):
    n = len(frame)
    if x+1 < n:
        if frame[x+1][y][PILLAR] and not is_pillar_possible(x+1, y, frame):
            return False
        if x-1 >= 0:
            if frame[x-1][y][FOUNDATION] and frame[x+1][y][FOUNDATION]:
                if not is_foundation_possible(x-1, y, frame) or not is_foundation_possible(x+1, y, frame):
                    return False
    if frame[x][y][PILLAR] and not is_pillar_possible(x, y, frame):
        return False
    return True
        
        
def solution(n, build_frame):
    answer = []
    n += 1
    frame = [[[False, False] for _ in range(n)] for _ in range(n)]
    
    for x, y, kind, operation in build_frame:
        if kind == PILLAR:
            if operation == 1:
                # 기둥 설치
                frame[x][y][PILLAR] = True
                # 가능성 검토
                is_possible = is_pillar_possible(x, y, frame)
                if not is_possible:
                    frame[x][y][PILLAR] = False # 롤백
            else:
                # 기둥 삭제
                frame[x][y][PILLAR] = False
                is_possible = is_pillar_delation_possible(x, y, frame)
                if not is_possible:
                    frame[x][y][PILLAR] = True # 롤백
        else:
            if operation == 1:
                # 보 설치
                frame[x][y][FOUNDATION] = True
                is_possible = is_foundation_possible(x, y, frame)
                if not is_possible:
                    frame[x][y][FOUNDATION] = False
            else:
                # 보 삭제
                frame[x][y][FOUNDATION] = False
                is_possible = is_foundation_delation_possible(x, y, frame)
                if not is_possible:
                    frame[x][y][FOUNDATION] = True # 롤백
        # print(f">> 가로좌표{x}, 세로좌표{y}, {'기둥' if kind == 0 else '보'}, {'설치' if operation == 1 else '삭제'}")
        # for i in range(n):
        #     print(frame[i])
    
    for i in range(n):
        for j in range(n):
            if frame[i][j][PILLAR]:
                answer.append([i, j, PILLAR])
            if frame[i][j][FOUNDATION]:
                answer.append([i, j, FOUNDATION])
        
    return answer

# solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])