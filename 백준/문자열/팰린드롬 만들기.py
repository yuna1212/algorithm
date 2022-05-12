"""
시작 시간: 2022년 5월 12일 오후 4시 5분
소요 시간: 1시간
풀이 방법:
    문자 교환해가면서 풀다가 안되겠어서 풀이 봤다.
    전체 문자 풀을 만들고 앞에서부터 알파벳 빠른 순으로 절반만큼 문자열을 만든다.
    중간 문자열이 있는 경우 추가하고,
    뒤에는 앞에 있던 문자열을 역순으로 붙여준다.
"""
from collections import Counter
def solution(string):
    alpha_counter = Counter(string)
    is_odd = False
    ret = []
    middle = ""
    
    # 개수가 홀수인 문자는 오직 string의 길이가 홀수 일 때, 딱 한 개만 허용됨
    for key, value in alpha_counter.items():
        if value % 2 == 1:
            if is_odd or len(string) % 2 == 0:
                return "I'm Sorry Hansoo"
            else:
                is_odd = True
                middle = key
                alpha_counter[key] -= 1
    
    alpha_kind = list(alpha_counter.keys())
    alpha_kind.sort()
    for alphabet in alpha_kind:
        while alpha_counter[alphabet]:
            ret.append(alphabet)
            alpha_counter[alphabet] -= 2
    return "".join(ret + list(middle) + list(reversed(ret)))

print(solution(input()))