"""
시작 시간: 2022-11-04 03:21 PM
소요 시간: 10분
풀이 방법: 문자열을 차례대로 읽으며 0->1과 1->0 지점 찾기
"""
s = input()
is_last_zero = True if s[0] == '0' else False
zero_count = 0
one_count = 0
if is_last_zero:
    one_count += 1
else:
    zero_count += 1

for c in s[1:]:
    if c == '0' and not is_last_zero:
        one_count += 1
        is_last_zero = True
    elif c == '1' and is_last_zero:
        zero_count += 1
        is_last_zero = False

print(min(zero_count, one_count))


