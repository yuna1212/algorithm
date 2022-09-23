"""
시작 시간: 2022-09-23 02:30 PM
소요 시간: 1시간 10분
풀이 방법:
    - 모르겠다
    - 2개의 group만 존재할 수 있다는걸 놓쳤다
"""
def find(editors, child):
    if editors[child] == child: return child
    editors[child] = find(editors, editors[child])
    return editors[child]

def union(editors, rank, big_child, small_child):
    big_child = find(editors, big_child)
    small_child = find(editors, small_child)
    if big_child==small_child:
        return
    if rank[big_child] < rank[small_child]: big_child, small_child = small_child, big_child
    editors[small_child] = big_child
    if rank[small_child] == rank[big_child]: rank[big_child] += 1
    return

def solution():
    n, m = map(int, input().split()) # 회원 수, 댓글 수
    editors = [n]*(n+1)
    rank = [1]*(n+1)
    dislikes = [set() for _ in range(n+1)]
    for i in range(m):
        kind, a, b = input().split()
        a, b= int(a), int(b)
        print('dislikes', dislikes)
        if kind == 'ACK':
            a, b = find(editors, a), find(editors, b)
            for dislike in dislikes[a]:
                if a == find(editors, dislike): return (False, i)
            union(editors, rank, a, b)
        else:
            a, b = find(editors, a), find(editors, b)
            if a == b: return (False, i)
            dislikes[a].add(b)
            dislikes[b].add(a)

    sizes = {}
    for editor in editors:
        editor = find(editors, editor)
        if editor in sizes:
            sizes[editor] += 1
        else:
            sizes[editor] = 1

    result_size = 0
    for key in sizes.keys():
        key = find(editors, key)
        if key == n: continue
        result_size = max(result_size, sizes[key])

    print('parents', editors)
    print('sizes', sizes)
    return (True, result_size + sizes[n]-1)
        
for _ in range(int(input())):
    result = solution()
    if result[0]:
        print('MAX PARTY SIZE IS', result[1])
    else:
        print('CONTRADICTION AT', result[1])
