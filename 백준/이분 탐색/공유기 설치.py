"""
시작 시간: 2022년 3월 3일 오후 2시 30분
소요 시간: 1시간 30분
풀이 방법:
    다음 링크 참고해서 풀이 확인
        https://velog.io/@seanlion/boj2110
    거리를 하나하나 탐색하면서 라우터를 몇 개 설치할 수 있을지 확인해야 하는 문제
    거리를 고정시키지 않아서 풀이 착안하지 못함
    거리를 선형적으로 확인하지 말고, 지수적으로 확인할 수 있을지 생각해보기
"""
N, C = map(int, input().split())
data = []
for i in range(N):
  data.append(int(input()))
 
data.sort()
 
start = 1 # 공유기 사이 거리 최솟값
end = data[-1] - data[0] # 공유기 사이 거리 최댓값
ans = []
 
while start <= end:
  prev = data[0] # 첫번째 집의 위치값
  mid = (start + end) // 2 # 중간 간격
  count = 1 # 라우터 개수. 첫번째 집에 라우터 설치
  for i in range(1, N):
    if prev + mid <= data[i]: # 이전집에서 중간간격만큼 떨어진것보다 바깥쪽에 있다면
      prev = data[i] # 라우터 추가
      count += 1
  if count >= C: # 원하던 개수보다 크게 설치할 수 있다면
    start = mid + 1 # 중간 간격을 하나 더 키워
    ans.append(mid)
  else:
    end = mid - 1
 
print(max(ans))