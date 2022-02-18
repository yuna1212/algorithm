"""
시작 시간: 2022년 2월 18일 오후 6시
소요 시간: 40분
풀이 방법:
    재귀로 품
"""
def isPrime(number):
    number = int(number)
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number**(1/2))+1):
        if number % i == 0:
            return False
    return True

def search(madeNum, numbers):
    global madeNums
    # 더이상 확인할 숫자 조합이 없으면
    if not numbers and int(madeNum) in madeNums:
        return 0
    count = 0
    # 해당 숫자가 이전에 없던 소수이면
    if int(madeNum) not in madeNums:
        if isPrime(madeNum):
            count += 1
            madeNums.append(int(madeNum))
    # 다음 소수 탐색
    for number in numbers:
        nextNums = numbers[:]
        nextNums.remove(number)
        count += search(madeNum + number, nextNums)
    return count
    
    
def solution(numbers):
    global madeNums
    madeNums = []
    numbers = list(numbers)
    ans = search("0", numbers)
    return ans

print(solution("011"))