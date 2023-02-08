"""
시작 시간: 2023-02-08 11:39 PM
소요 시간: 2시간 30분
풀이 방법:
"""
class Node():
    def __init__(self, position, priority):
        self.position = position
        self.priority = priority
        self.previous = None
        self.next = None
    
    def __repr__(self):
        return "position: "+str(self.position)+" priority: "+str(self.priority)

    def delete(self, cost):
        cost -= self.get_distance_from(self.previous) + self.get_distance_from(self.next)
        print('삭제연산!!!!!!')
        if self.previous:
            self.previous.next = self.next
            cost += self.previous.get_distance_from(self.next)

        if self.next:
            self.next.previous = self.previous

        return cost

    def add(self, node, cost):
        cost -= self.get_distance_from(self.next)
        cost += self.get_distance_from(node)
        cost += node.get_distance_from(self.next)

        if self.next:
            self.next.previous = node
            node.next = self.next

        self.next = node
        node.previous = self
        return cost

    def get_distance_from(self, node):
        if node == None:
            return 0
        return abs(self.position - node.position)


n, k = map(int, input().split())
priorities = list(map(int, input().split()))

window = []
for i in range(k):
    window.append((priorities[i], i))
window.sort()
print(window)

left_node = Node(window[0][1], window[0][0])
node = left_node
answer = 0
for i in range(1, k):
    next_node = Node(window[i][1], window[i][0])
    answer = node.add(next_node, answer)
    node = node.next

cost = answer
for i in range(k, n):
    extra_node = Node(i, priorities[i])
    node = left_node
    print('----------------')
    print('i', i)
    print('시작 비용', cost)
    added = False
    deleted = False
    while not (added and deleted):
        # extra node를 추가
        print('node', node)
        if node.position == i - k:
            # 윈도우 제일 왼쪽의 노드를 삭제
            print('제일 왼쪽 삭제', node.priority)
            tmp = node
            node = node.next
            cost = tmp.delete(cost)
            print('삭제 후 남은 비용', cost)
            print('node', node)
            deleted = True 
            continue

        if node.priority > extra_node.priority: 
            # 노드를 앞에 추가
            cost = extra_node.add(node, cost)
            added = True
            print('앞에 추가 후 남은 비용', cost)

        elif not node.next:
            # 노드를 가장 끝에 추가
            cost = node.add(extra_node, cost)
            added = True
            print('끝에 추가 후 남은 비용', cost)

        node = node.next

    answer = min(answer, cost)
    left_node = left_node.next
    while left_node.previous:
        left_node = left_node.previous
            
print(answer)
