"""
시작 시간: 2022-10-19 02:23 AM
소요 시간: 20분
풀이 방법: 1부터 차례로 더하다가, s보다 커지면 그 차만큼 '해당하는 숫자'만 제해주면 된다. 해당하는 숫자는 마지막으로 더한 숫자보다 작은 숫자일 수 밖에 없다.
"""
s = int(input())
n = 1
count = 0
while s >= 0:
    s -= n
    count += 1
    n += 1
print(count - 1)
