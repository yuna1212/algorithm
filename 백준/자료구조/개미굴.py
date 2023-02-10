"""
시작 시간: 2023-02-10 06:37 PM
소요 시간: 40분
풀이 방법: 각 음식을 노드에 저장하는 트라이 생성. 깊이 15 이하이기에 충분히 가능!
"""
def update(trie, info):
    for w in info:
        if w not in trie:
            trie[w] = dict()

        trie = trie[w]

def print_structure(trie, step):
    for food in sorted(trie.keys()):
        print('--'*step+food)
        if trie[food]:
            print_structure(trie[food], step+1)

n = int(input())
trie = dict()
for _ in range(n):
    foods = list(input().split())[1:]
    update(trie, foods)

print_structure(trie, 0)
