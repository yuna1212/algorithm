"""
시작 시간: 2022-11-24 06:03 PM
소요 시간: 50분
풀이 방법: 점화식 도출은 생각보다 쉽지만, 관건은 0을 처리하는 방법. 예를 들어..
    - 201의 0은 해석할 수 있다.
    - 901의 0은 해석할 수 없다
"""
def is_decodable(ten, one):
    if ten == '0':
        return False
    ascii_code = int(ten)*10 + int(one)
    return 1 <= ascii_code <= 26

password = input()
last = old = now = 1
if password[0] == '0':
    print(0)
else:
    for i in range(1, len(password)):
        now = last
        if password[i] == '0':
            now = 0
        else:
            now = last
        
        if is_decodable(password[i-1], password[i]):
            now += old
            now %= 1000000
        old = last
        last = now
    print(now)
