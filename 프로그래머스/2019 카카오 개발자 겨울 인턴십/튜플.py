"""
시작 시간: 2022년 5월 3일 오후 5시 10분
소요 시간: 35분
풀이 방법:
    차집합 구하기 또는 정규식 활용
    정규식 쓰는게 훨씬 효율이 좋았다.
"""
def solution(s):
    s = s[1:-1]
    answer = []
    sets_length_of = [set()]
    # 스트링 읽어서 배열에 저장
    a_set = set()
    number = ''
    for i, kind in enumerate(s):
        if kind == "{":
            a_set = set()
        elif kind == "}":
            a_set.add(int(number))
            number = ''
            sets_length_of.append(a_set)
        elif kind == ",":
            if number:
                a_set.add(int(number))
                number = ''
        else:
            number += kind
    sets_length_of.sort(key = lambda x: len(x))
    # 튜플 만들기
    for i in range(1, len(sets_length_of)):
        difference = sets_length_of[i] - sets_length_of[i-1]
        answer.append(list(difference)[0])
    return answer
import re
def solution2(s):    
    s = s[1:-1]
    answer = []
    sets_length_of = [set()]
    # 스트링 읽어서 배열에 저장
    tuples = re.findall(r'\{(.*?)\}', s)
    for t in tuples:
        if len(t) > 1:
            t = set(map(int, t.split(',')))
            sets_length_of.append(t)
        else:
            sets_length_of.append(set([int(t)]))
    sets_length_of.sort(key = lambda x: len(x))
    # 튜플 만들기
    for i in range(1, len(sets_length_of)):
        difference = sets_length_of[i] - sets_length_of[i-1]
        answer.append(list(difference)[0])    
    return answer
print(solution2("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    
    
    