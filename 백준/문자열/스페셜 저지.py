"""
시작 시간: 2022년 5월 16일 오후 7시 40분
소요 시간: 20분
풀이 방법:
    기존에 작성한 kmp 모듈 그대로 사용하여 해결
"""
def make_table(pattern):
    pattern_size = len(pattern)
    table = [0] * pattern_size
    j = 0
    for i in range(1, pattern_size):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table
def kmp(sentence, pattern, pattern_table):
    ret = []
    sentence_size = len(sentence)
    pattern_size = len(pattern)
    j = 0
    for i in range(0, sentence_size):
        while j > 0 and sentence[i] != pattern[j]:
            j = pattern_table[j-1]
        if sentence[i] == pattern[j]:
            if j == pattern_size - 1:
                ret.append(i - pattern_size + 1)
                j = pattern_table[j]
            else:
                j += 1
    return ret

def solution(a, b, sub_string):
    table = make_table(sub_string)
    if kmp(a, sub_string, table) and kmp(b, sub_string, table):
        print("YES")
    else:
        print("NO")
solution(input(), input(), input())