"""
시작 시간: 2022-09-06 AM 09:59
소요 시간: 1시간
풀이 방법:
    - combination 모듈을 쓰지 않았다.
    - stack을 사용해서 재귀 없이 combination을 구현했다.
    - 서로 다른 팀을 구하기 위해 list 타입의 stack을 set로 변경해서 차집합을 구했다
"""
def input_data():
    global STATS, N, PLAYERS
    STATS = []
    N = int(input())
    PLAYERS = set(i for i in range(N))
    for _ in range(N):
        line = list(map(int, input().split()))
        STATS.append(line)

def get_team_stat(team):
    global STATS
    team_stat = 0
    for i in team:
        for j in team:
            if i == j: continue
            team_stat += STATS[i][j]
    return team_stat

def get_diff(team):
    global N, PLAYERS
    other_team = PLAYERS - team
    return abs(get_team_stat(team) - get_team_stat(other_team))


global STATS, N
input_data()
answer = 1000
team_size = N//2

for base_player_id in range(N):
    stack = [base_player_id]
    player_id = base_player_id+1
    while stack:
        if len(stack) < team_size and player_id < N:
            stack.append(player_id)
            player_id += 1
            continue

        if len(stack) == team_size:
            # 팀이 결정됨
            answer = min(answer, get_diff(set(stack)))

        player_id = stack.pop() + 1
print(answer)

