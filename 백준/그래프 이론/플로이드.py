"""
시작 시간: 2023-03-11 01:31 AM
소요 시간: 30분
풀이 방법: 최단거리 한 개의 최댓값이 A -> B의 최단거리보다 작을 수 있음에 유의
"""
import sys
input = sys.stdin.readline
INF = 100000*100

n = int(input().rstrip())
m = int(input().rstrip())
distance = [[INF]*n for _ in range(n)]


for _ in range(m):
    i, j, cost = map(int, input().rstrip().split())
    i -= 1; j -= 1;
    distance[i][j] = min(cost, distance[i][j])


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j: continue
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for line in distance:
    for d in line:
        if d == INF:
            print(0, end= " ")
        else:
            print(d, end= " ")
    print()

