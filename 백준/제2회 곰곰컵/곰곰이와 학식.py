"""
시작 시간: 2023-01-23 10:33 PM
소요 시간: 20분
풀이 방법:
"""
hungries = list(map(int, input().split()))
tickets = list(map(int, input().split()))

before_counting = sum(hungries)
for _ in range(2):
    for i in range(3):
        if hungries[i] >= tickets[i]:
            hungries[i] -= tickets[i]
            tickets[i] = 0
        else:
            tickets[i] -= hungries[i]
            hungries[i] = 0
            
            # 티켓 교환
            tickets[(i+1)%3] += tickets[i] // 3
            tickets[i] %= 3

print(before_counting - sum(hungries))

