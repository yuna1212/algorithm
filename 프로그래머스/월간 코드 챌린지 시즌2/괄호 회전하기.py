"""
시작 시간: 2022년 6월 13일 오후 12시 15분
소요 시간: 15분
풀이 방법: 스택으로 적합한 괄호문장인지 판별
"""
from collections import deque
BRACKET_DICT = {"(":")", "[":"]", "{":"}"}
def is_validate_bracket_pair(first, second):
    if first in BRACKET_DICT:
        if second == BRACKET_DICT[first]:
            return True
        return False
    return False
def is_validate_sentence(sentence):
    stack = []
    for bracket in sentence:
        if stack and is_validate_bracket_pair(stack[-1], bracket):
            stack.pop()
        else:
            stack.append(bracket)
    if stack:
        return False
    return True
def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        mover = s.popleft()
        s.append(mover)
        answer += is_validate_sentence(s)
    return answer
print(solution(	"}]()[{"))