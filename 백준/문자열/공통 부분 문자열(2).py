"""
시작 시간: 2022년 5월 12일 오후 1시 25분
소요 시간: 20분 
풀이 방법:
    무식하게 풀기
"""
def solution(s1, s2):
    loggest_common_length = 0
    i = 0
    while i <= len(s1) - loggest_common_length:
        j = 0
        while j <= len(s1) - loggest_common_length:
            loggest_common_length = get_loggest_common_length(s1[i:], s2[j:], loggest_common_length)
            j += 1
        i += 1
    return loggest_common_length

def get_loggest_common_length(sub_s1, sub_s2, loggest_common_length):
    if sub_s1[:loggest_common_length] != sub_s2[:loggest_common_length]: # 가장 긴 공통 길이보다 작은 길이에서 문자열 안일치하면
        return loggest_common_length
    
    while loggest_common_length < len(sub_s1) and loggest_common_length < len(sub_s2): # 매개변수값보다 큰 가장 긴 공통 길이 구하기
        if sub_s1[loggest_common_length] != sub_s2[loggest_common_length]:
            break
        loggest_common_length += 1
    return loggest_common_length

print(solution(input(), input()))