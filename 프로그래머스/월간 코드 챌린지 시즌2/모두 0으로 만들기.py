"""
시작 시간: 2022년 6월 13일 오후 12시 20분
소요 시간: 50분
풀이 방법: 위상정렬로 풀었는데 시간초과....

"""

"""
아래 풀이는 덜 완성된 위상정렬.
히든테케에서 군데군데 실패로 뜬다.
자식 노드 -> 부모 노드로 가중치를 넘겨야 하는데,
아래 풀이는 역으로 가중치를 넘기게 될 수도 있기 때문이다.
"""
"""
from collections import deque
def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    # connections: 인접리스트로 트리 표현
    tree_size = len(a)
    answer = 0
    connections = [[] for _ in range(tree_size)]
    for u, v in edges:
        connections[u].append(v)
        connections[v].append(u)
    
    queue = deque()
    for i, connection in enumerate(connections):
        if len(connection) == 1:
            queue.append(i) # 모든 리프 노드를 큐에 넣기
    
    visited = [False] * tree_size
    
    while queue: # 모든 노드 탐색
        node_number = queue.popleft()
        if visited[node_number]: # 방문한 노드라면 패스
            continue
        if a[node_number] != 0: # 가중치 넘길 노드 찾기
            for connected_node_number in connections[node_number]: 
                if not visited[connected_node_number]: # 현재 노드의 가중치를 연결된 노드로 넘기기
                    answer += abs(a[node_number])
                    a[connected_node_number] += a[node_number]
                    a[node_number] = 0        
                    break
        
        if a[node_number] != 0: # 가중치를 0으로 만들 수 없음
            return -1
        
        visited[node_number] = True
        queue += connections[node_number] # 연결된 노드들 큐에 넣기
    
    return answer
print(solution([-2, 8, -5, -5, -3, 0, 5, 2], [[0, 1], [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7]]))
"""
def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    # connections: 인접리스트로 트리 표현
    tree_size = len(a)
    answer = 0
    connections = [[] for _ in range(tree_size)]
    for u, v in edges:
        connections[u].append(v)
        connections[v].append(u)
    
    stack = []
    topology_degree = [0] * tree_size
    for i, connection in enumerate(connections):
        topology_degree[i] = len(connection)
        if topology_degree[i] == 1:
            stack.append(i) # 모든 리프 노드를 스택에 넣기
    
    while stack:
        while stack: # 모든 노드 탐색
            node_number = stack.pop()
            if a[node_number] != 0: # 가중치 넘길 노드 찾기
                for connected_node_number in connections[node_number]: 
                    if topology_degree[connected_node_number] > 0: # 현재 노드의 가중치를 연결된 노드로 넘기기
                        answer += abs(a[node_number])
                        a[connected_node_number] += a[node_number]
                        a[node_number] = 0 
                        for connected_node_number in connections[node_number]:
                            topology_degree[connected_node_number] -= 1
                        break
            
            if a[node_number] != 0: # 가중치를 0으로 만들 수 없음
                return -1
            topology_degree[node_number] -= 1
            
        for i, degree in enumerate(topology_degree):
            if degree == 1:
                stack.append(i)
    return answer
solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]])