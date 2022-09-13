"""
- 시간 복잡도: O(단어길이 * 단어 개수)
- 인접 행렬을 이용한다.
    - 사이즈는 충분히 작다: 인접 행렬의 크기는 26*26으로 900이 안되고, 0/1만 저장하므로 사이즈는 충분히 작다.
- 위상 정렬은 한다.
    - 사이클 유무와 관계 없이 위상정렬만 하면 된다.
    - 사이클이 있다면 위상정렬이 되지 않는다.
    - 위상정렬이 된다면 위상정렬 결과를 받으면 된다.
- dfs 하면서 방문하는 정점들을 순서대로 저장한다.
- dfs 하며 저장한 정점들은 위상정렬 되어있다고 가정한다.
    - 위상정렬 되어있다면, 연결된 정점들은 모두 한쪽방향만 존재할 것이다.
    - 모든 위상정렬된 정점들을 방문하면서 반대방향은 없는지 확인한다.
- 위상정렬 리스트에 추가할 때 마지막 것 부터 추가하는 이유
    - !! dfs 시작점이 root라는 것을 보장할 수 없기에!!
"""
ADJ = None
SEEN, ORDER = [], [] 


def make_graph(words):
    global ADJ
    ADJ = [[0]*26 for _ in range(26)]
    for j in range(1, len(words)):
        i = j - 1
        length = min(len(words[i]), len(words[j]))
        for k in range(0, length):
            if words[i][k] != words[j][k]:
                # 먼저오는 알파벳 -> 뒤에 오는 알파벳 만 표시한다.
                a = ord(words[i][k]) - ord('a')
                b = ord(words[j][k]) - ord('a')
                ADJ[a][b] = 1
                break

def dfs(here):
    global SEEN, ADj, ORDER
    SEEN[here] = 1
    for there in range(len(ADJ)):
        if ADJ[here][there] and not SEEN[there]:
            dfs(there)
    ORDER.append(here)

def topological_sort():
    global ADJ, SEEN, ORDER
    m = len(ADJ)
    SEEN = [0] * m
    ORDER.clear()
    for i in range(m):
        if not SEEN[i]: dfs(i)
    ORDER.reverse()
    for i in range(m):
        for j in range(i+1, m):
            if ADJ[ORDER[j]][ORDER[i]]:
                return None
    return ORDER

make_graph(['gg', 'kia', 'lotte', 'lg', 'hanwha'])
result = topological_sort()
if result:
    for char in topological_sort():
        print(chr(char+65), end="")
else:
    print("INVALID")
print()    
