"""
시작 시간: 2023-03-02 04:03 PM
소요 시간: 1시간 10분
풀이 방법: 플로이드 와샬
    - 문제 조건에 두 지점을 연결하는 도로가 여럿 있을 수 있다고 했다.
    - 이거 놓쳐서 좀 헤맴,,
    - 조건을 잘 확인하자
"""
import sys
input = sys.stdin.readline
MAX_COST = 10000

def maybe_past(dist):
    min_dists = [[MAX_COST]*len(dist) for _ in range(len(dist))]
    for k in range(len(dist)):
        for i in range(len(dist)):
            for j in range(len(dist)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                if i == j and dist[i][i] < 0:
                    return True

    for i in range(len(dist)):
        if dist[i][i] < 0:
            return True
    
    return False

def solution():
    n, m, w = map(int, input().rstrip().split())
    dist = [[MAX_COST+1]*n for _ in range(n)]
    for _ in range(m):
        s, e, t = map(int, input().rstrip().split())
        s -= 1
        e -= 1
        dist[s][e] = min(t, dist[s][e])
        dist[e][s] = dist[s][e]

    for _ in range(w):
        s, e, t = map(int, input().rstrip().split())
        s -= 1
        e -= 1
        dist[s][e] = -t

    if maybe_past(dist):
        print("YES")
    else:
        print("NO")


for _ in range(int(input().rstrip())):
    solution()
