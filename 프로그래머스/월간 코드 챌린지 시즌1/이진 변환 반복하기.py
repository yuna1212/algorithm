"""
시작 시간: 2022년 5월 31일 오후 3시 20분
소요 시간: 20분
풀이 방법:
    string 잘 다뤄서 풀기
    2진수 만들어야 할 10진수는 string의 '길이'인 것에 유의하기
"""
def solution(s):
    bins_counter = 0
    zeros_counter = 0
    bin_length = len(s)
    
    while bin_length > 1:
        the_num_of_zero = s.count('0')
        zeros_counter += the_num_of_zero
        bin_length -= the_num_of_zero
        s = str(bin(bin_length))[2:]
        bin_length = len(s)
        bins_counter += 1
    return bins_counter, zeros_counter
print(solution("110010101001"))