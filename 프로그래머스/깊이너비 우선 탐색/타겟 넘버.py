"""
시작 시간: 2022년 3월 26일 오전 1시 10분
소요 시간: 20분
풀이 방법:
    - BFS로 품: O(2^N)이지만 어차피 입력이 최대 20개라 크게 영향x(테케 최악이 0.5초정도 나옴)
    - 덧셈 뺄셈이라길래 이항연산만 생각했는데, 첫번째 수가 음수일 수도 있다는게 함정....아니;;
"""
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    i = 0
    queue.append((i, numbers[0]))
    queue.append((i, -numbers[0]))
    while queue:
        i, made = queue.popleft()
        if i < len(numbers)-1:
            i += 1
            queue.append((i, made + numbers[i]))
            queue.append((i, made - numbers[i]))
        else:
            if made == target:
                answer += 1
    return answer
