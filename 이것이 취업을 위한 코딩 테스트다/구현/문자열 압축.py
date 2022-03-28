"""
시작 시간: 2022년 3월 28일 오후 2시 40분
소요 시간: 1시간 10분
풀이 방법:
    - 히든에서 틀림,, 44점
    - 인덱스를 경우에 따라 옮겨주는 방식
"""
def solution(s):
    answer = len(s)
    for k in range(1, len(s)//2+1):
        unit = s[:k]
        unit_count = 1
        packing_len = 0
        i = k
        while i <= len(s)-k:
            next = s[i:i+k]
            i += k
            if next == unit:
                # 기준 문자열과 동일할 때
                unit_count += 1
            else:
                # 기준 문자열과 다를 때
                if unit_count > 1:
                    # 여태까지 압축해온 길이가 1보다 크다면
                    packing_len += 1 + k
                    unit_count = 1
                else:
                    # 압축이 안되었다면
                    packing_len += k
                unit = next # 새로운 기준 단위
            if packing_len > answer:
                break
        # 처리 못한 중복자들
        if unit_count > 1:
            packing_len += 1+k
            i += k
        else:
            packing_len += k
        # 처리 못한 남는 문자들
        if i < len(s):
            packing_len += len(s) - i
        if packing_len < answer:
            answer = packing_len
    return answer
print(solution("ababcdcdababcdcd"))