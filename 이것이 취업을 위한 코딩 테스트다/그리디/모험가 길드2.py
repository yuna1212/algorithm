"""
시작 시간: 2022년 3월 24일 오후 1시 10분
소요 시간: 20분
풀이 방법:
    기존에 그룹이 이미 만들어져있다고 가정하고 논리를 구성한게 문제다.
    그룹이 만들어져있지 않다고 생각하고 다시 보기!
"""
# 입력
_ = input()
people = list(map(int, input().split()))
people.sort()

the_number_of_group = 0
how_many_in_last_group = 0
for person in people:
    if how_many_in_last_group + 1 > person:
        # 그룹 분할
        the_number_of_group += 1
        how_many_in_last_group = person
    elif how_many_in_last_group + 1 < person:
        # 더이상 그룹 구성 불가
        break
    else:
        # 기존 그룹에 추가
        how_many_in_last_group += 1
print(the_number_of_group)