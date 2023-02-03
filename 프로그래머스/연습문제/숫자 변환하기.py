"""
시작 시간: 2023-02-03 11:55 AM
소요 시간: 1시간
풀이 방법: 어차피 주기마다 큐 바꿔줘서, 큐 말고 리스트로 다뤄도 충분
"""
from collections import deque

def solution(x, y, n):
    answer = 0
    checked = set()
    queue = deque([x]) 

    while True:
        next_queue = deque()

        while queue:
            x = queue.popleft()

            if x in checked:
                continue
            
            checked.add(x)

            if x == y:
                return answer

            elif x < y:
                next_queue.append(x+n)
                next_queue.append(x*2)
                next_queue.append(x*3)

        if not next_queue:
            break 

        queue = next_queue
        answer += 1

    return -1 

print(solution(10, 40, 5))
