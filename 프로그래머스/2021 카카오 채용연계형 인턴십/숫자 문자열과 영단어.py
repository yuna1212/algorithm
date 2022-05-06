"""
시작 시간: 2022년 5월 6일 오후 2시 50분
소요 시간: 40분
풀이 방법:
    정규표현식으로 어떻게 풀 수 있을까
"""
def solution(s):
    i = 0
    answer = ""
    number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    while i < len(s):
        if s[i].isdigit():
            answer += s[i]
            i += 1
        else:
            for j, number in enumerate(number_words):
                if s[i:i+len(number)] == number:
                    answer += str(j)
                    i += len(number)
                    break
    return answer