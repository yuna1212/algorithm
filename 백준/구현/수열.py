"""
시작 시간: 2022-11-02 02:31 PM
소요 시간: 10분
풀이 방법: 슬라이딩 윈도우
"""
n, k = map(int, input().split())
temperatures = list(map(int, input().split()))
window = sum(temperatures[:k])
max_sum = window 
for i in range(n-k):
    window = window - temperatures[i] + temperatures[i+k]
    max_sum = max(max_sum, window)
print(max_sum)
