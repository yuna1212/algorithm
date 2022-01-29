"""
시작 시간: 2022년 1월 29일 오후 7시 5분
소요 시간: 2시간
풀이 방법:
    4가지 블럭중, 하얀색 빈칸이 위치할 수 있는 경우를 나눠 총 12가지에 대해
    차례로 모든 하얀색 빈칸에 맞추어보았다.
    중복을 제거하지 않아 실패..
"""
from sys import stdin
# 12개의 L자 블럭
BLOCKS = [[[1, 0], [1, 1]], [[-1, 0], [0, 1]], [[0, -1], [-1, -1]],
          [[1, 0], [0, 1]], [[-1, 0], [-1, 1]], [[0, -1], [1, -1]],
          [[0, 1], [1, 1]], [[0, -1], [1, 0]], [[-1, 0], [-1, -1]],
          [[1, 0], [1, -1]], [[0, -1], [-1, 0]], [[0, 1], [-1, 1]]]


def board(whiteSpaces):
    if not whiteSpaces:
        # 흰색 칸을 모두 덮었을 때
        return 1

    countMethods = 0
    for i, whiteSpace in enumerate(whiteSpaces):
        # 덮이지 않은 모든 흰색칸 탐색
        for block in BLOCKS:
            # 주어진 흰색 칸을 모든 종류의 블록으로 덮어본다
            blockPortions = [[whiteSpace[0]+block[0][0], whiteSpace[1]+block[0][1]],
                             [whiteSpace[0]+block[1][0], whiteSpace[1]+block[1][1]]]
            if blockPortions[0] in whiteSpaces and blockPortions[1] in whiteSpaces:
                # 해당 위치를 적절히 덮는다면
                nowWhiteSpaces = whiteSpaces[:]
                nowWhiteSpaces.remove(whiteSpace)
                nowWhiteSpaces.remove(blockPortions[0])
                nowWhiteSpaces.remove(blockPortions[1])
                countMethods += board(nowWhiteSpaces)  # 덮은 후 다음 흰색 자리에서 탐색
    return countMethods


# input
for _ in range(int(input())):
    height, width = map(int, stdin.readline().split())
    whiteSpaces = []
    for h in range(height):
        row = stdin.readline()
        for w in range(len(row)):
            if row[w] == ".":
                whiteSpaces.append([h, w])
    print(board(whiteSpaces))
