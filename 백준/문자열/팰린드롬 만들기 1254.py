"""
시작 시간: 2022년 5월 12일 오후 5시 10분
소요 시간: 20분
풀이 방법:
    완성될 팰린드롬의 '길이'를 기준으로, 해당 문자열의 길이부터 길이의 2배까지 반복문 돌림(문자열은 최대 길이가 50이므로 충분히 가능)
    만약 팰린드롬이 가능한 문자열이라면, 그 길이 출력하고 프로그램 종료
"""
def solution(string):
    ret = len(string)
    for ret in range(ret, len(string)*2):
        if is_palindrom(string, ret):
            return ret
    return len(string)*2

def is_palindrom(string, target_length):
    for i in range(target_length - len(string), target_length // 2):
        if string[i] != string[target_length-i-1]:
            return False
    return True

print(solution(input()))