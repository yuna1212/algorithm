"""
시작 시간: 2022년 3월 30일 오후 1시 25분
소요 시간: 30분
풀이 방법:
    O(N^2)로 해결
    그냥 단순하게 반복문 두번 돌림
"""

# 입력
n, m = map(int, input().split())
bowling_balls = list(map(int, input().split()))

result = 0
for i in range(0, len(bowling_balls)):
    last_ball = bowling_balls[i]
    for j in range(i+1, len(bowling_balls)):
        now_ball = bowling_balls[j]
        if now_ball == last_ball:
            continue
        result += 1
        
print(result)