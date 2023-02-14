"""
시작 시간: 2023-02-14 12:51 PM
소요 시간: 50분
풀이 방법: 연산 순서 잘 확인하기. 값을 다시 대입한 후, 이전 값을 생각하고 다루지는 않았는지 체크하기
"""
def get_subnumbers(n, k):
    subnumbers = []
    r = -1
    subnumber = []
    while not (n == 0 and r == 0):
        r = n % k
        n = n // k
        if r == 0:
            if subnumber:
                subnumber.reverse()
                subnumbers.append(int(''.join(map(str, subnumber))))
                subnumber = []
        else:
            subnumber.append(r)

    return subnumbers

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n**0.5+1)):
        if n%i == 0:
            return False
    return True 

def solution(n, k):
    answer = 0
    numbers = get_subnumbers(n, k)
    for number in numbers:
        if is_prime(number):
            answer += 1

    return answer
