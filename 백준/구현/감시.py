"""
시작 시간: 2022-11-29 01:15 AM
소요 시간: 1시간 50분
풀이 방법: 복잡한 데이터를 상수로 저장하기 위해 수기로 작성할때는 꼼꼼하게 확인하기
"""
import sys
input = sys.stdin.readline
MAP = []
CCTVS = [] # CCTV[i] = (x, y), CCTV 위치 정보 저장
CCTV_TURNING_VECTORS = [
    None,
    [[[0, 1]], [[1, 0]], [[0, -1]], [[-1, 0]] ],
    [[[0, -1], [0, 1]], [[-1, 0], [1, 0]]],
    [[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[0, -1], [1, 0]], [[-1, 0], [0, -1]]],
    [[[0, -1], [-1, 0], [0, 1]], [[-1, 0], [0, 1], [1, 0]], [[0, -1], [1, 0], [0, 1]], [[0, -1], [1, 0], [-1, 0]]],
    [[[0, -1], [-1, 0], [0, 1], [1, 0]]]
] # CCTV_TURNING_VECTORS[CCTV_kind][turning_case] 는 특정 cctv 종류에 대해 감시 벡터 표현
MONITORED = 9

def unmark(monitoring_spot):
    """ monitoring_spot의 위치를 모두 빈 공간으로 표시 """
    for x, y in monitoring_spot:
        if MAP[x][y] == MONITORED:
            MAP[x][y] = 0

def mark_and_get_monitoring_spot(cctv_idx, turning_idx):
    """ 해당 cctv와 주어진 회전 경우에 대해, 감시 영역을 표시하고 표시된 감시 영역을 반환 """
    x, y = CCTVS[cctv_idx]
    cctv_kind = MAP[x][y]
    diffs = CCTV_TURNING_VECTORS[cctv_kind][turning_idx]
    monitoring_spot = []

    for dx, dy in diffs:
        nx, ny = x, y
        while True:
            nx += dx
            ny += dy

            if not ( 0 <= nx < N and 0 <= ny < M) or MAP[nx][ny] == 6: break # 범위를 벗어나거나 벽이면 해당 방향 그만 탐색
            if 1 <= MAP[nx][ny] <= 5: continue # 다른 CCTV면 pass

            if MAP[nx][ny] == 0:
                MAP[nx][ny] = MONITORED 
                monitoring_spot.append((nx, ny))
    return monitoring_spot

def get_blind_spot_size():
    """ 지도에서 사각 지대의 크기를 반환 """
    ret = 0
    for x in range(N):
        for y in range(M):
            if MAP[x][y] == 0:
                ret += 1
    return ret

def get_min_blind_spot_size(cctv_idx):
    """ 최소 사각지대 영역을 재귀로 구하기 """
    if cctv_idx == len(CCTVS):
        return get_blind_spot_size()

    x, y = CCTVS[cctv_idx]
    cctv_kind = MAP[x][y]
    min_blind_spot_size = N*M

    next_cctv_idx = cctv_idx+1
    for turning_idx in range(len(CCTV_TURNING_VECTORS[cctv_kind])):
        monitoring_spot = mark_and_get_monitoring_spot(cctv_idx, turning_idx)
        min_blind_spot_size = min(min_blind_spot_size, get_min_blind_spot_size(next_cctv_idx))
        unmark(monitoring_spot)

    return min_blind_spot_size

N, M = map(int, input().rstrip().split())
for i in range(N):
    MAP.append(list(map(int, input().rstrip().split())))
    for j in range(M):
        if 1 <= MAP[i][j] <= 5:
            CCTVS.append((i, j))

if CCTVS:
    print(get_min_blind_spot_size(0))
else:
    print(get_blind_spot_size())
