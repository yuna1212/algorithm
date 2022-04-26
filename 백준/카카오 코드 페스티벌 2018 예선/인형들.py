"""
시작 시간: 2022년 4월 26일 오후 1시 5분
소요 시간: 30분
풀이 방법:
    풀이는 쉬운데 다음 어려움이 있었다,,
    1. 표준 편차를 계산하기 위해 고르는 인형의 개수가 K개 이상일 수도 있다는 것을 캐치 못함
        K개 이상이더라도, O(N^2) 시간복잡도가 나오는데 이게 맞는지 헷갈렸음
        하지만 인형의 개수는 500개라서 완전탐색으로도 충분히 가능하다고 판단
    2. 분산의 최댓값을 1로 고정시켜버림.. 그래서 계속 오답처리됨. 분산 최댓값이 1이 초과될 수 있다는걸 깜빡함
    3. 평균을 위해 sum 구하는 과정에서 시간 더 절약할 수 있지만, 어차피 큰 차이도 없고 이렇게 풀어도 문제 없으므로 그냥 품
"""
def get_variance(numbers):
    avg = sum(numbers)/len(numbers)
    var = 0
    for number in numbers:
        var += (number - avg) ** 2
    return var/len(numbers)

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
min_variance = get_variance([0, 10**6])
for i in range(k, n+1):
    for j in range(0, n - i + 1):
        var = get_variance(numbers[j:j+i])
        min_variance = min(var, min_variance)
print(min_variance ** 0.5)