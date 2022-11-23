"""
시작 시간: 2022-11-23 07:10 PM
소요 시간: 1시간 10분
풀이 방법: 문제 이해가 오래거렸다.. 정렬과 그리디로 풀이
"""
n = int(input()) # 센서 개수
k = int(input()) # 집중국 개수
sensors = sorted(list(map(int, input().split())))
distances = []
for i in range(1, n):
    distances.append(sensors[i] - sensors[i-1])
distances.sort(reverse=True)
ans = 0
for i in range(k-1, n-1):
    ans += distances[i]
print(ans)
