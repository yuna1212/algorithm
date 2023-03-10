"""
시작 시간: 2023-03-11 05:25 AM
소요 시간: 1시간
풀이 방법: 읽기 쉬운 코드를 작성해야 디버깅도 편하다,,
    - 몇 사분면인지 저장하는 변수를 선언하면 n==1일 때 처리 같이할 수 있으니까 분기문 양이 적어진다
"""
def solution(start_r, start_c, n):
    global r, c, result
    half = 2**(n-1)
    next_r, next_c = r, c
    quad = 0
    quad_diff = ((0, 0), (0, half), (half, 0), (half, half))

    if r < half + start_r:
        if c < half + start_c:
            quad = 0
        else:
            quad = 1
    else:
        if c < half + start_c:
            quad = 2
        else:
            quad = 3

    result += half*half*quad

    if n > 1:
        solution(start_r+quad_diff[quad][0], start_c+quad_diff[quad][1], n-1)

result = 0
n, r, c = map(int, input().split())
solution(0, 0, n)
print(result)
