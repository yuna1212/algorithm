"""
시작 시간: 2022년 3월 4일 오후 1시 15분
소요 시간: 2시간
풀이 방법:
    다음 수로 연결할 수 있는 모든 수들의 인덱스를 pointers 리스트에 저장
    pointers를 거꾸로 읽으면서, max_lengths에 해당 위치에서 가질 수 있는 길이들을 계산하여 최댓값만 저장
    무식하게 풀면 O(2^N), DP로 풀면 O(N^2)
"""
from sys import stdin
# 입력
_ = input()
NUMBERS = list(map(int, stdin.readline().split()))

# 연결될 수 있는 다음 숫자들의 주소 저장
pointers = []
for i in range(len(NUMBERS)):
    nexts = []
    pointers.append(nexts)
    for j in range(i+1, len(NUMBERS)):
        if NUMBERS[i] < NUMBERS[j]:
            nexts.append(j)

max_lengths = [-1] * len(NUMBERS)
for i in range(len(NUMBERS) - 1, -1, -1):
    if pointers[i]:
        lengths = []
        for next in pointers[i]:
            lengths.append(max_lengths[next] + 1)
        max_lengths[i] = max(lengths)
    else:
        max_lengths[i] = 1
print(max(max_lengths))