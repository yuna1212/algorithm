"""
시작 시간: 2022-11-17 03:12 PM
소요 시간: 30분
풀이 방법:
"""
import sys
input = sys.stdin.readline

def get_max_score(sticker):
    if len(sticker[0]) == 1:
        return max(sticker[0][0], sticker[1][0])
    sticker[0][1] += sticker[1][0]
    sticker[1][1] += sticker[0][0]
    for i in range(2, len(sticker[0])):
        sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
        sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])
    return max(sticker[0][len(sticker[0])-1], sticker[1][len(sticker[0])-1])

for _ in range(int(input().strip())):
    n = int(input().strip())
    sticker = []
    sticker.append(list(map(int, input().strip().split())))
    sticker.append(list(map(int, input().strip().split())))
    print(get_max_score(sticker))

