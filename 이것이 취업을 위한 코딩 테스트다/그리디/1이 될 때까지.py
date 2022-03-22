"""
시작 시간: 2022년 3월 22일 오후 1시 10분
소요 시간: 20분
풀이 방법:
    k로 최대한 많이 나누도록 한다
"""
n, k = map(int, input().split())
counter = 0
while n > 1:    
    q = n // k
    counter += n - (q*k) + 1# 가장 가까운 k의 배수로 이동하고 k로 나누기 위한 횟수
    n = q
print(counter)