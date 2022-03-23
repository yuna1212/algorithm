"""
시작 시간: 2022년 3월 23일 오후 2시 20분
소요 시간: 20분
풀이 방법:
    조합 공식 이용 -> for문 너무 많이돌아서 시간 오래걸림
    다른 방법 찾기
"""
import time
def combinate(n, r):
    # nCr 구하기
    denominator = 1 # 분모
    numerator = 1 # 분자
    for i in range(r):
        numerator *= n-i
        denominator *= r-i
    return int(numerator/denominator)

# 입력
n, m = map(int, input().split())
bowling_balls = sorted(list(map(int, input().split())))
combination_count = combinate(n, 2)
# 중복 구하기
start = time.time()
print(start)
bowling_balls_set = set(bowling_balls)
repeates = []
for bowling_ball in bowling_balls_set:
    bowling_ball_count = bowling_balls.count(bowling_ball)
    if bowling_ball_count > 1:
        repeates.append(bowling_ball_count)
# 중복 제거
for count in repeates:
    repeat_comb = combinate(count, 2)
    combination_count -= repeat_comb
print(combination_count)
end = time.time()
print(end)
print("소요시간:", (end - start)*100000)

# 정답 solution
start = time.time()
array = [0]*11
for x in bowling_balls:
    array[x] += 1
result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i]*n
print(result)
end = time.time()
print("소요시간:", (end - start)*100000)