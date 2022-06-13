"""
시작 시간: 2022년 6월 13일 오전 11시 40분
소요 시간: 15분
풀이 방법: 제곱수는 약수의 개수가 홀수개이다,,, 임을 활용하면 10줄 안으로 끝남
"""
def get_sign(number):
    aliquot = 0
    root_value = int(number**0.5)
    
    for i in range(1, root_value):
        if number % i == 0:
            aliquot += 2
    if number % root_value == 0:
        if root_value*root_value == number:
            aliquot += 1
        else:
            aliquot += 2
    if aliquot % 2 == 0:
        return 1
    return -1

def solution(left, right):
    answer = 0
    for number in range(left, right+1):
        sign = get_sign(number)
        answer += sign*number
    return answer

### 제곱수는 약수의 개수가 홀수개인 점을 이용
def more_solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer