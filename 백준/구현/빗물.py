"""
시작 시간: 2022년 4월 13일 오후 4시 30분
소요 시간: 20분
풀이 방법:
    간단한 구현 문제
    주어진 데이터 구간도 몹시 작고, 시간복잡도 생각 안하고 풀어도 통과
"""
H, W = map(int, input().split())
heights = list(map(int, input().split()))
left_highest, right_highest = heights[0], max(heights[1:])
result = 0
for i in range(1, W-1):
    left_highest, right_highest = max(heights[:i]), max(heights[i+1:])
    height = heights[i]
    x = min(left_highest, right_highest) - height
    if x > 0:
        result += x
print(result)