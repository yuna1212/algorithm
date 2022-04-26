"""
시작 시간: 2022년 4월 26일 오후 3시 10분
소요 시간: 2시간
풀이 방법:
    80퍼센트 쯤에서 시간초과가 난다.
    다른 사람들 풀이를 봐도, 푸는 방법은 틀리지 않았다.
    탐색 과정에서 오버헤드가 발생한다는데, 지금은 못찾겠다..
    링크 https://www.acmicpc.net/board/view/86503 참조해보자
"""
from sys import stdin
def is_unition_possible(num1, num2):
    global L, R
    if L <= abs(num1 - num2) <= R:
        return True
    return False
def get_party(x, y):
    global A
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = [(x, y)]
    visited = [[False for _ in range(len(A))] for _ in range(len(A))]
    neighbor = []
    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        neighbor.append((x, y))
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0<=nx<len(A) and 0<=ny<len(A):
                if is_unition_possible(A[x][y], A[nx][ny]):
                    stack.append((nx, ny))
    return neighbor
        
N, L, R = map(int, stdin.readline().split())
A = []
for _ in range(N):
    line = list(map(int, stdin.readline().split()))
    A.append(line)
is_moved = True
day = 0
while is_moved:
    is_moved = False
    x, y = 0, 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    parties = []
    for x in range(0, N):
        for y in range(0, N):
            if visited[x][y]:
                continue
            party = get_party(x, y)
            if len(party) > 1:
                for nx, ny in party:
                    visited[nx][ny] = True
                parties.append(party)   
    if parties:
        is_moved = True
        for party in parties:
            people_count = sum([A[x][y] for x, y in party]) // len(party)
            for x, y in party:
                A[x][y] = people_count
    if is_moved:
        day += 1
print(day)