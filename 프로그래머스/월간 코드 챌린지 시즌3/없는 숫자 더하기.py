"""
시작 시간: 2022년 6월 14일 오후 5시 20분
소요 시간: 1분
풀이 방법: 집합 연산
"""
def solution(numbers):
    all_numbers = set(i for i in range(0, 10))
    return sum(all_numbers - set(numbers))