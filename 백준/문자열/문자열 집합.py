"""
시작 시간: 2022년 5월 12일 오후 1시 50분
소요 시간: 15분
풀이 방법:
    검사할 문자열들을 순서대로 집합에 있는지 확인
"""
from sys import stdin
def get_set_and_inspecting_words():
    n, m = map(int, input().split())
    set_s = set()
    for _ in range(n):
        set_s.add(stdin.readline().rstrip())
    words_inspecting = []
    for _ in range(m):
        words_inspecting.append(stdin.readline().rstrip())
    return set_s, words_inspecting

def solution(a_set, inspecting_words):
    ret = 0
    for inspecting in inspecting_words:
        if inspecting in a_set:
            ret += 1
    return ret
a_set, get_set_and_inspecting_words = get_set_and_inspecting_words()
print(solution(a_set, get_set_and_inspecting_words))