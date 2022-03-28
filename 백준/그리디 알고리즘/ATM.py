"""
시작 시간: 2022년 3월 28일 오후 12시 50분
소요 시간: 5분
풀이 방법:
    people[i], 1<=i<-n일 때, 
    sum(people) = n*people[1]+(n-1)people[2]+(n-2)people[3]+...+people[n] 임을 적용
"""
n = int(input())
people = list(map(int, input().split()))
people.sort()

result = 0
for i in range(0, n):
    person = people[i]
    result += (n-i)*person
print(result)    