"""
시작 시간: 2023-01-24 10:52 PM
소요 시간: 50분
풀이 방법: 초등학교 수학 문제 풀이
"""
import heapq
n, l = map(int, input().split()) # 치킨 개수, 시소 길이
positions = tuple(map(int, input().split()))
weights = tuple(map(int, input().split()))

denominator = sum(weights)
numerator = 0
for i in range(n):
    numerator += weights[i] * positions[i]

print(round(numerator / denominator, 6))




