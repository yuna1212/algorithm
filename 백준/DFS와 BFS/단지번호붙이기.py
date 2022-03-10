"""
시작 시간: 2022년 3월 10일 오후 4시
소요 시간: 50분
풀이 방법:
    너비 우선 탐색으로, 특정 집 기준 인접한 집들의 개수 구함
    방문한 집은 지도에서 지워버려서 전체 탐색에서 더이상 탐색 안되도록 함
    아니면 visited 리스트를 따로 둬서 거기에 있는지 확인할수도 있겠지만, 지도의 변경 유무가 중요하진 않고 지도 변경하면 메모리도 적게 사용하기에 이렇게 구현
"""
########## 데이터 입력 ##########
N = int(input())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, list(input()))))

########## 너비우선탐색 ##########
def count_adjacent_house(start):
    global N, MAP
    will_visit = [start]
    counter = 0
    while will_visit:
        now = will_visit.pop(0)
        counter += 1
        now_row = now // N
        now_column = now % N
        MAP[now_row][now_column] = 0 # 방문한 집은 지도에서 지우기
        # 오른쪽
        if now_column + 1 < N and MAP[now_row][now_column+1] > 0 \
            and now_row*N+now_column+1 not in will_visit:
            will_visit.append(now_row*N+now_column+1)
        # 아래쪽
        if now_row + 1 < N and MAP[now_row+1][now_column] > 0 \
            and (now_row+1)*N+now_column not in will_visit:
            will_visit.append((now_row+1)*N+now_column)
        # 왼쪽
        if now_column - 1 >= 0 and MAP[now_row][now_column-1] > 0 \
            and now_row*N+now_column-1 not in will_visit:
            will_visit.append(now_row*N+now_column-1)
        # 위쪽
        if now_row - 1 >= 0 and MAP[now_row-1][now_column] > 0 \
            and (now_row-1)*N+now_column not in will_visit:
            will_visit.append((now_row-1)*N+now_column)
    return counter

########## 전체 맵 순차 탐색 ##########
results = []
for i in range(N):
    for j in range(N):
        if MAP[i][j] > 0:
            results.append(count_adjacent_house(i*N+j))

########## 답 출력 ##########
results.sort()
print(len(results))
for r in results:
    print(r)