"""
시작 시간: 2022년 6월 16일 오후 3시
소요 시간: 15분
풀이 방법: 간단한 BFS
"""
from collections import deque
def visit(visited, computer_idx, computers):
    queue = deque()
    queue.append(computer_idx)
    while queue:
        computer_idx = queue.popleft()
        if visited[computer_idx]:
            continue
        visited[computer_idx] = True
        for i in range(len(computers)):
            if computers[computer_idx][i]:
                queue.append(i)
    return
def solution(n, computers):
    answer = 0
    computer_idx = 0
    visited = [False] * n
    while computer_idx < n:
        if not visited[computer_idx]:
            visit(visited, computer_idx, computers)
            answer += 1
        computer_idx += 1
    return answer