"""
시작 시간: 2022년 3월 30일 오후 2시 10분
소요 시간: 40분
풀이 방법:
    사람 한명씩 볼 때마다, 새로운 팀을 구성할 수 있는지 확인
    아래 코드를 최적화하면 결국 책으 정답 코드가 됨
"""
# 입력
_ = input()
people = list(map(int, input().split()))
people.sort()

group_count = 0
needs = 0
now = 0
for i in range(0, len(people)):
    score = people[i]
    now += 1 # 예비 팀에 현재 사람 추가
    if score != needs:
        needs = score # 예비 팀의 공포도와 다르다면 바꿔주기
    
    if needs == now:
        # 팀 조건 충족했다면
        group_count += 1
        now = 0
        
print(group_count)