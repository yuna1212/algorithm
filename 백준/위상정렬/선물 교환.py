"""
시작 시간: 2022-09-13 04:36 PM
소요 시간: 1시간
풀이 방법:
- 시간초과와 틀렸습니다......
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def input_data():
global GRAPH, GAVE, GIVEN
    n = int(input().strip())
    GRAPH = [[] for _ in range(n)]
    for i in range(n):
        j, k = map(int, input().strip().split())
        GRAPH[i].append(j-1)
        GRAPH[i].append(k-1)

def dfs(giver, selected):
    global GRAPH, GAVE, GIVEN
    if GAVE[giver]:
        return selected
    GAVE[giver] = True
    for taker in GRAPH[giver]:
        if GIVEN[taker] < 2:
            GIVEN[taker] += 1
            if dfs(taker, selected) is None:
                return
        else:
            return
    selected.add(giver+1)
    return selected

def solve():
    global GRAPH, GAVE, GIVEN
    n = len(GRAPH)
    answer = []
    for giver in range(len(GRAPH)):
        GAVE = [ False ] * n
        GIVEN = [ 0 ] * n
        result = set()
        if dfs(giver,result):
            if sum(GIVEN) == len(result)*2:
                answer = result if len(result) > len(answer) else answer
    return answer

input_data()
result = solve()
if result:
    result = list(result)
    result.sort()
    print(len(result))
    print(' '.join(map(lambda x: str(x), result))
else:
    print(0)



