"""
시작 시간: 2022년 6월 23일 오후 2시 35분
소요 시간: 1시간
풀이 방법: BFS
"""
from collections import deque
def is_connected(a_word, other_word):
    size = len(a_word)
    has_diff = False
    for i in range(size):
        if a_word[i] != other_word[i]:
            if has_diff:
                return False
            has_diff = True
    return has_diff

def make_graph(words):
    graph = [[] for _ in range(len(words))]
    for i, word in enumerate(words):
        for j in range(i+1, len(words)):
            if is_connected(word, words[j]):
                graph[i].append(j)
                graph[j].append(i)
    return graph

def bfs(begin_idx, target_idx, graph):
    visited = [False]*len(graph)
    queue = deque()
    queue.append((begin_idx, 0))
    while queue:
        word_idx, path = queue.popleft()
        if visited[word_idx]:
            continue
        if word_idx == target_idx:
            return path
        visited[word_idx]  = True
        for next_word in graph[word_idx]:
            queue.append((next_word, path+1))
    return 0

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    words.append(begin)
    graph = make_graph(words)
    answer = bfs(words.index(begin), words.index(target), graph)
    return answer