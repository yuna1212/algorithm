"""
시작 시간: 2023-01-23 10:23 PM
소요 시간: 10분
풀이 방법:
"""
from sys import stdin
input = stdin.readline

dancing_people = set()
dancing_people.add("ChongChong")

for _ in range(int(input().rstrip())):
    one, another = input().rstrip().split()

    if one in dancing_people:
        dancing_people.add(another)
    elif another in dancing_people:
        dancing_people.add(one)

print(len(dancing_people))

