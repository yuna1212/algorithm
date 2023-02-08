"""
시작 시간: 2023-02-09 11:23 AM
소요 시간: 1시간
풀이 방법: 시간초과
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
        cost -= self.get_distance(self.previous) + self.get_distance(self.next)
        if self.previous:
            self.previous.next = self.next

        if self.next:
            self.next.previous = self.previous

        if self.next and self.previous:
            cost += self.previous.get_distance(self.next)


        return cost

    def add(self, node, cost):
        # self 뒤에 node 추가
        cost -= self.get_distance(self.next)
        cost += self.get_distance(node)
        cost += node.get_distance(self.next)

        if self.next:
            self.next.previous = node
            node.next = self.next

        self.next = node
        node.previous = self
        return cost

    def insert(self, node, cost):
        # self의 앞에 node 추가
        cost -= self.get_distance(self.previous)
        cost += self.get_distance(node)
        cost += node.get_distance(self.previous)

        if self.previous:
            self.previous.next= node
            node.previous= self.previous

        self.previous = node
        node.next= self
        return cost

    def get_distance(self, node):
        if node == None:
            return 0
        return abs(self.position - node.position)

n, k = map(int, input().split())
priorities = list(map(int, input().split()))

if k == 1:
    print(0)
    exit()

window = []
for i in range(k):
    window.append((priorities[i], i))
window.sort()

start_node = Node(window[0][1], window[0][0])
node = start_node
cost = 0
for i in range(1, k):
    next_node = Node(window[i][1], window[i][0])
    cost = node.add(next_node, cost)
    node = node.next

answer = cost
for i in range(k, n):
    extra_node = Node(i, priorities[i])
    added = False
    deleted = False
    if start_node.next:
        start_node = start_node.next
    while start_node.previous:
        start_node = start_node.previous

    node = start_node
    while not (added and deleted):
        if node.position == i - k:
            # 노드 삭제
            tmp = node
            if node.next:
                node = node.next
            else:
                node = node.previous
            cost = tmp.delete(cost)
            deleted = True
            continue

        if not added and node.priority > extra_node.priority:
            # 노드를 앞에 추가
            cost = node.insert(extra_node, cost)
            added = True
        elif not added and not node.next:
            # 노드를 가장 끝에 추가
            cost = node.add(extra_node, cost)
            added = True

        node = node.next
    
    answer = min(answer, cost)

print(answer)

