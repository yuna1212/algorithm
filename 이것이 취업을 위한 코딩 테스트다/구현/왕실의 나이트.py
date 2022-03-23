"""
시작 시간: 2022년 3월 23일 오후 5시 35분
소요 시간: 15분
풀이 방법:
    가능한 L자 움직임을 튜플에 저장해두고, 튜플의 모든 원소를 탐색함
"""
# 입력
data = input()
column = ord(data[0]) - ord('a')
row = int(data[1]) - 1

counter = 0
movable_units = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
for movable_unit in movable_units:
    movable_row, movable_column = movable_unit
    next_row, next_column = row+movable_row, column+movable_column
    if 0<=next_row<=9 and 0<=next_column<=9:
        counter += 1
print(counter)