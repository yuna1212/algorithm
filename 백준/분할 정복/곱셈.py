"""
시작 시간: 2022년 2월 22일 오전 10시 55분
소요 시간: 10분
풀이 방법:
    행렬 제곱 문제와 풀이 동일
    곱셈의 결합법칙에서 풀이 착안
"""
global c
a, b, c = map(int, input().split())
def multiply(a, b):
    global c
    if b == 1:
        return a % c
    if b%2 == 0:
        partition = multiply(a, b//2) % c
        return partition*partition % c
    partition = multiply(a, b//2)
    return partition*partition*a%c
print(multiply(a, b))