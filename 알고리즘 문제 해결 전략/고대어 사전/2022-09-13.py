"""
시작 시간: 2022-09-13 01:25 PM
소요 시간: 1시간 20분
풀이 방법:
     - 시간복잡도 O(N^2): N은 전체 단어에서 등장한 알파벳의 개수
     - 더이상 연결되는 문자가 없는 문자를 매번 탐색
        - 각 탐색마다 추가적으로 한번씩 더 순회..k
"""

def make_graph(dictionary):
    graph = {}
    for i in range(len(dictionary)-1):
        precending_word = dictionary[i]
        following_word = dictionary[i+1]
        for j in range(min(len(precending_word), len(following_word))):
            precending_alphabet = precending_word[j]
            following_alphabet = following_word[j]
            if precending_alphabet != following_alphabet:
                if precending_alphabet in graph:
                    graph[precending_alphabet].add(following_alphabet)
                else:
                    graph[precending_alphabet] = set([following_alphabet])
                if following_alphabet not in graph:
                    graph[following_alphabet] = set() 
                break
    return graph

def find_roots(graph):
    roots = []
    for key, values in graph.items():
        if len(values) == 0:
            roots.append(key)
    return roots

def solve(graph):
    sorted_alphabets = []
    roots = find_roots(graph)
    while roots:
        for root in roots: 
            sorted_alphabets.append(root)
            del graph[root]
            for key, value in graph.items():
                if root in value:
                    graph[key].remove(root)
        roots = find_roots(graph)
    if len(graph.keys()) > 0:
        return None
    return sorted_alphabets

all_alphabets = set('abcdefghijklmnopkrstuvwxyz')
for _ in range(int(input())):
    n = int(input())
    dictionary = []
    for _ in range(n):
        dictionary.append(input())
    graph = make_graph(dictionary)
    ans = solve(graph)
    if(ans):
        rest = all_alphabets - set(ans)
        ans.reverse()
        ans += rest
        print(''.join(ans))

    else:
        print("INVALID HYPOTHESIS")


