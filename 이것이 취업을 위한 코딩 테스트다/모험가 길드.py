"""
시작 시간: 2022년 3월 22일 오후 5시 5분
소요 시간: 45분
풀이 방법:
    공포도순으로 사람 정렬 후, 최대한 새로운 그룹을 만들게끔
    이 풀이도 틀리진 않았지만, 이것보다 더 추상적으로 푸는 방법 생각해보기
        - 메모리랑 코드 덜 써서 짜보기
"""
# 입력
_ = input()
people = list(map(int, input().split()))
people.sort()
def is_valid(sorted_group):
    # 주어진 그룹이 가능한 것인지 확인하는 메소드
    if not sorted_group:
        # 그룹에 아무도 없으면
        return False
    if sorted_group[-1] > len(sorted_group):
        # 가장 높은 공포도보다 인원이 적으면
        return False
    return True

# 그룹 분할 시작
groups = []
for person in people:
    if not groups:
        # 가장 용감한 사람
        groups.append([person])
        continue
    last_group = groups[-1]
    if len(last_group) > person:
        new_group = last_group[len(last_group)-person+1:] + [person]
        if is_valid(new_group) and is_valid(last_group[:len(last_group)-person+1]):
            groups[-1] = last_group[:len(last_group)-person+1]
            groups.append(new_group)
            continue
    if is_valid(last_group + [person]):
        last_group.append(person)
    else:
        break
print(len(groups))