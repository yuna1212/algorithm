"""
시작 시간: 2023-01-23 11:01 PM
소요 시간: 1시간
풀이 방법: 마지막에 분기를 잘 못나눠서 문제를 해맸다..
"""
from sys import stdin
input = stdin.readline

n = int(input().rstrip())
most_left_index = most_upward_index = n
most_right_index = most_downward_index = 0
for i in range(n):
    line = input().rstrip()
    for j in range(n):
        if line[j] == "G":
            most_left_index = min(most_left_index, j)
            most_right_index = max(most_right_index, j)
            most_upward_index = min(most_upward_index, i)
            most_downward_index = max(most_downward_index, i)

answer = 0
if most_right_index != most_left_index:
    # 왼쪽 또는 오른쪽으로
    answer += min(most_right_index, - most_left_index + n - 1)
if most_downward_index != most_upward_index:
    # 위 또는 아래로
    answer += min(most_downward_index, - most_upward_index + n - 1)
print(answer)

