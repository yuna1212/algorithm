"""
시작 시간: 2022년 8월 30일 오전 10시 35분
소요 시간: 10분
풀이 방법:
    스택 사용하지 않고 구현.
    여는 괄호가 앞서 몇 개 나왔는지 확인한다.
"""
def check(string):
    the_number_of_brackets = 0
    for char in string:
        if char == "(":
            the_number_of_brackets += 1
        else:
            the_number_of_brackets -= 1
        if the_number_of_brackets < 0:
            return False 
    if the_number_of_brackets == 0:
        return True
    return False

for _ in range(int(input())):
    result = check(input())
    if(result):
        print("YES")
    else:
        print("NO")
