"""
시작 시간: 2022년 3월 16일 오후 2시 5분
소요 시간: 1시간
풀이 방법: 
    지나친 경로는 다시 방문 안하는걸로
    매번 리스트 새로 할당해서 씀 -> 재할당 비용과 deque에서 popleft 쓰는거랑 뭐가 더 클까?
    리스트를 재할당하면 pop할 이유가 없다. 실제로 테스트했을 때 그냥 할당해서 쓰는게 시간 덜씀
"""
# 입력
N, M = map(int, input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, list(input()))))

# 이동해보기
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0] # 왼 오 위 아
positions = [(0, 0)]
path_length = 1
is_done = False
while not is_done:
    new_positions = []
    for position in positions:
        x, y = position
        if x == N-1 and y == M-1:
            # 마지막 위치에 왔으면 경로 출력
            print(path_length)
            is_done = True
            break
    
        for i in range(4):
            if 0<=x+dx[i]<N and 0<=y+dy[i]<M and MAP[x+dx[i]][y+dy[i]] == 1:
                # 방문하지 않은 이동 가능한 상하좌우 탐색
                MAP[x+dx[i]][y+dy[i]] += 1
                new_positions.append([x+dx[i],y+dy[i]])
    path_length += 1
    positions = new_positions