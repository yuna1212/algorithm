"""
시작 시간: 2022년 3월 23일 오전 11시 25분
소요 시간: 2분
풀이 방법:
    직접 연산한 결과를 비교..했으나
    비교하지 않고도 주어진 수를 비교하여 최적의 연산을 수행할 수 있음
        i) a = 0, b = 0 -> 곱셈, 덧셈 결과 동일
        ii) a = 0, b > 0 또는 a > 0, b = 0 -> 덧셈
        iii) a > 0, b > 0 -> 덧셈이 더 좋은 결과이기위해선 1/a + 1/b > 1이어야하므로,
             a 또는 b가 1일 때 덧셈
"""
s = input()
# solution 1
result = 0
for number in s:
    number = int(number)
    result = max(result*number, result+number)
print(result)

# solution 2
result = 0
for number in s:
    number = int(number)
    if result < 2 or number < 2:
        result += number
    else:
        result *= number
print(result)