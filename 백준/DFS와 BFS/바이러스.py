"""
시작 시간: 2022년 6월 21일 오후 11시 45분
소요 시간: 10분
풀이 방법: 간단한 DFS
"""
def input_data():
    n = int(input())
    m = int(input())
    computers = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        computers[x].append(y)
        computers[y].append(x)
    return computers

computers = input_data()
visited = [False] * len(computers)
stack = [1]

while stack:
    infected_computer = stack.pop()
    if visited[infected_computer]:
        continue
    visited[infected_computer] = True
    for connected_computer in computers[infected_computer]:
        stack.append(connected_computer)
print(sum(visited)-1)    