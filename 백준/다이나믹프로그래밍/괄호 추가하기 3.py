"""
시작 시간: 2022-11-28 04:24 PM
소요 시간: 1시간 
풀이 방법: 
    - 1차원 점화식으로 해결이 어렵다면 2차원으로 풀이할 수 없을까 고민해보기
    - 예전 블로그 풀이 본 거 기억나서 그대로 구현
"""
n = int(input())
numbers = []
operators = []
line = input()
def operate(preceding_number, following_number, operator):
    if operator == "+":
        return preceding_number + following_number
    if operator == "-":
        return preceding_number - following_number
    if operator == "*":
        return preceding_number * following_number

for i in range(1, n-1, 2):
    numbers.append(int(line[i-1]))
    operators.append(line[i])
numbers.append(int(line[-1]))

size = len(numbers)
dp = [[None]*size for _ in range(size)]
for i in range(size):
    dp[i][i] = [numbers[i], numbers[i]] # 최소, 최대
for k in range(1, size):
    for i in range(size-k):
        j = i + k
        min_result = max_result = operate(dp[i][i][0], dp[i+1][j][0], operators[i])
        for l in range(i, j):
            for m in range(2):
                for n in range(2):
                    result = operate(dp[i][l][m], dp[l+1][j][n], operators[l])
                    min_result = min(min_result, result)
                    max_result = max(max_result, result)
        dp[i][j] = (min_result, max_result)

print(dp[0][size-1][1])
