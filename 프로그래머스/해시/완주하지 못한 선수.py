"""
시작 시간: 2022년 2월 28일 오후 10시 55분
소요 시간: 1시간
풀이 방법:
    completion을 순회하면서 participant에서 원소 삭제 -> O(N*M), N은 participant 길이, M은 completion 길이
    Counter 객체로 딕셔너리로 바꿈. value는 원소 개수 -> O(N+M)
"""
from collections import Counter
""" 첫번째 풀이: 선형 탐색 """
# def solution(participant, completion):
#     for c in completion:
#         if c in participant:
#             participant.remove(c)
#     return participant[0]

""" 두번째 풀이: 딕셔너리로 바꿔서, 등장 개수를 value로 저장 """
def solution(participant, completion):
    participantDict = Counter(participant)
    completionDict = Counter(completion)
    answer = list((participantDict - completionDict).keys())[0]
    return answer