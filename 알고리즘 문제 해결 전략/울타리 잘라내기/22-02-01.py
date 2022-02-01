"""
시작 시간: 2022년 1월 29일 오후 10시 40분
소요 시간: 30분
풀이 방법:
    분할정복은 아니지만 O(n^2)의 시간복잡도로 모든 경우의 수를 구했다.
"""
from sys import stdin

def cut(fences):
    maxArea = 0
    for fenceIndex in range(len(fences)):
        area = (fenceIndex+1)*min(fences[:fenceIndex+1])
        maxArea = max(maxArea, area)
    return maxArea

def tryCutting(fences):
    maxArea = 0
    for i in range(len(fences)):
        maxArea = max(maxArea, cut(fences[i:]))
    return maxArea

for _ in range(int(input())):
    int(input())
    fences = list(map(int, stdin.readline().split()))
    print(">>> ", tryCutting(fences))