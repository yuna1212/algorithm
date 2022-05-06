"""
시작 시간: 2022년 5월 4일 오전 2시 50분
소요 시간: 50분
풀이 방법:
    중복을 어떻게 없애지..?
"""
import re
def solution(user_id, banned_id):
    answer = 1
    patterns = []
    for b in banned_id:
        patterns.append(b.replace("*", "\w"))
    for pattern in patterns:
        same_pattern_user_count = 0
        for user in user_id:
            if re.fullmatch(pattern, user):
                print(pattern.replace("\w", "*"), user)
                same_pattern_user_count += 1
        answer *= same_pattern_user_count
    return answer
solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])