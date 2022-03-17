"""
시작 시간: 2022년 3월 16일 오후 12시 50분
소요 시간: 50분
풀이 방법:
    - 매일매일 영향있는 토마토가 있는지 확인
    - 있다면 전부 꺼내서 새로운 익은 토마토 만들 수 있는지 확인
    - 새롭게 만든 익은 토마토들은 다시 영향있는 토마토에 이어붙이고 날짜 하루 더해줌
    - collections 모듈의 deque 사용했으나 스택처럼 써서 list랑 차이 없음
    - 왼쪽 오른쪽을 dx, dy 리스트로 표현하면 코드 양 줄어든다..!
    - 생각해보니 굳이 while문에서 pop 쓰지 말고 for문으로 읽기만하고
        새로운 리스트를 붙이지말고 할당하는게 더 효과적일듯
"""
from collections import deque
# 입력
M, N = map(int, input().split())
tomato_box = []
for _ in range(N):
    tomato_box.append(list(map(int, input().split())))

# 원래 익어있던 토마토 찾기
influential_tomatos = deque([])
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 1:
            influential_tomatos.append([i, j])

# 날짜별로 토마토 찾기
day = 0
while influential_tomatos:
    new_influential_tomatos = []
    while influential_tomatos:
        ripen_tomato = influential_tomatos.pop()
        nx, ny = ripen_tomato[0], ripen_tomato[1]
        # 왼쪽
        if ny-1 >= 0 and tomato_box[nx][ny-1] == 0:
            new_influential_tomatos.append([nx, ny-1])
            tomato_box[nx][ny-1] = 1
        # 오른쪽
        if ny+1 < M and tomato_box[nx][ny+1] == 0:
            new_influential_tomatos.append([nx, ny+1])
            tomato_box[nx][ny+1] = 1
        # 위쪽
        if nx-1 >= 0 and tomato_box[nx-1][ny] == 0:
            new_influential_tomatos.append([nx-1, ny])
            tomato_box[nx-1][ny] = 1
        # 아래쪽
        if nx+1 < N and tomato_box[nx+1][ny] == 0:
            new_influential_tomatos.append([nx+1, ny])
            tomato_box[nx+1][ny] = 1
    if new_influential_tomatos:
        influential_tomatos.extend(new_influential_tomatos)
        day += 1
# 토마토가 다 익었는지 확인
are_ripen = True
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 0:
            are_ripen = False
            break
    if not are_ripen:
            break
if are_ripen:
    print(day)
else:
    print(-1)