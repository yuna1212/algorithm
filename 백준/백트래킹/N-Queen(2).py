"""
시작 시간: 2023-03-08 03:40 PM
소요 시간: 1시간 30분
풀이 방법: 가능한 퀸의 경우의 수가 아니라 N개 두는 경우의 수
    - 퀸은 같은 행, 열에는 두개 이상 존재할 수 없다 -> 1차원 배열로 나타낼 수 있다.
    - N개를 둔다면, 각 행마다 한 개의 퀸이 있어야 한다.
    - 가장 윗 행부터 아래로 탐색하면서 둘 수 있는 열이 있는지 확인하기
"""

def validate(x):
    global queens, result, n
    y = queens[x]
    for ix in range(x):
        iy = queens[ix]
        if iy == y or abs(iy - y) == x - ix:
            return False

    return True

def nqueen(x):
    global queens, result, n
    if x == n:
        result += 1
        return

    for y in range(n):
        queens[x] = y
        if validate(x):
            nqueen(x+1)

n = int(input())
queens = [0]*n
result = 0
nqueen(0)

print(result)
