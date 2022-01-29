"""
시작 시간: 2022년 1월 29일 오후 3시 30분
소요 시간: 2시간
풀이 방법:
    주어진 친구쌍에서, 모든 학생이 짝지을 수 있는 모든 경우를 탐색
"""
from sys import stdin


def picinic(selected, relations):
    # 종결조건
    if len(selected) == studentCount:
        # 유효한 쌍들로 마무리
        return 1
    if not relations:
        # 유효하지 않은 쌍들
        return 0

    # 부분문제
    countPairs = 0

    for i, selectedStudent in enumerate(relations):
        nowSelected = selected[:]
        nowSelected += [selectedStudent[0], selectedStudent[1]]
        availableRelations = relations[i:]
        # 짝을 이룬 학생이 포함된 관계 삭제
        availableRelations = list(filter(
            lambda x: selectedStudent[0] not in x and selectedStudent[1] not in x, availableRelations))

        countPairs += picinic(nowSelected[:], availableRelations)
    return countPairs


for _ in range(int(input())):
    studentCount, relationsCount = map(int, stdin.readline().split())
    relationsInput = list(map(int, stdin.readline().split()))
    relations = []
    for i in range(0, len(relationsInput), 2):
        relations.append((relationsInput[i], relationsInput[i+1]))
    print(f'>>> {picinic([], relations)}')
