"""
시작 시간: 2022년 3월 29일 오후 4시 45분
소요 시간: 20분
풀이 방법:
    퀵소트
"""
# 입력
n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

def quick_sort(data, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and data[left] >= data[pivot]:
            left += 1
        while right > start and data[right] <= data[pivot]:
            right -= 1
        if left > right:
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[right], data[left] = data[left], data[right]
    quick_sort(data, start, right-1)
    quick_sort(data, right+1, end)

quick_sort(data, 0, len(data)-1)
print(data)
    