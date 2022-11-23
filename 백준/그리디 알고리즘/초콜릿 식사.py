"""
시작 시간: 2022-11-23 08:20 PM
소요 시간: 30분
풀이 방법: 모든 수는 2의 제곱수들과 1의 합으로 구할 수 있다. 값 초기화에 주의 
"""
k = int(input())
min_chocolate_size = 1
while min_chocolate_size < k:
    min_chocolate_size *= 2
squared_number = min_chocolate_size
summing = 0
slicing_counter = 0
while k != summing:
    if squared_number + summing <= k:
        summing += squared_number
    squared_number //= 2
    slicing_counter += 1
print(min_chocolate_size, slicing_counter-1)
