"""
시작 시간: 2022-09-29 05:19 PM
소요 시간: 1시간 30분
풀이 방법:
    - 1시간정도 생각한 후 풀이 컨셉을 확인했다.
    - s를 t로 만드는게 아니라 t에서 가장 마지막 문자를 지우면서 s를 만든다
"""
from collections import deque
s = list(input())
t = deque(input())
is_reversed = 0
while len(t) > len(s):
    c = ''
    if is_reversed:
        c = t.popleft()
    else:
        c = t.pop()
    if c == 'B': 
        is_reversed = (is_reversed+1)%2 

answer = 1
if is_reversed:
    for i in range(len(s)):
        if s[i] != t[len(s)-i-1]:
            answer = 0
            break
else:
    for i in range(len(s)):
        if s[i] != t[i]:
            answer = 0
            break
print(answer)
