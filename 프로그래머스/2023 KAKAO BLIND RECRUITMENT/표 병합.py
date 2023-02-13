"""
시작 시간: 2023-02-13 02:42 PM
소요 시간: 2시간 10분
풀이 방법: 일부 틀림 
"""
class Group:
    def __init__(self, table_size):
        self.parent = []
        self.heights = []
        self.table_size = table_size
        for r in range(self.table_size):
            line = []
            for c in range(self.table_size):
                line.append((r, c))
            self.parent.append(line)
            self.heights.append([0]*self.table_size)
        
    def find(self, r, c):
        if self.parent[r][c] == (r, c):
            return r, c
        self.parent[r][c] = self.find(*self.parent[r][c])
        return self.parent[r][c]

    def merge(self, r1, c1, r2, c2):
        r1, c1 = self.find(r1, c1) # 그룹 대표
        r2, c2 = self.find(r2, c2)
        if self.heights[r1][c1] < self.heights[r2][c2]:
            r1, r2 = r2, r1
            c1, c2 = c2, c1

        self.parent[r2][c2] = r1, c1

        if self.heights[r1][c1] == self.heights[r2][c2]:
            self.heights[r1][c1] += 1

    def unmerge(self, r, c):
        r, c = self.find(r, c)
        unmerged_positions = []
        for x in range(self.table_size):
            for y in range(self.table_size):
                if self.find(x, y) == (r, c):
                    self.parent[x][y] = (x, y)
                    self.heights[x][y] = 0
                    unmerged_positions.append((x, y))

        return unmerged_positions

class Table:
    def __init__(self):
        self.size = 50
        self.table = [["EMPTY" for _ in range(self.size)] for _ in range(self.size)]
        self.group = Group(self.size)

    def empty(self, positions):
        for (r, c) in positions:    
            self.table[r][c] = "EMPTY"

    def get(self, r, c):
        r, c = self.group.find(r, c)
        return self.table[r][c]

    def set(self, r, c, value):
        r, c = self.group.find(r, c)
        self.table[r][c] = value

class Executor:
    def __init__(self, table):
        self.table = table
        self.result = []

    def run(self, command):
        command, *params = command.split()
        if command == "UPDATE":
            if len(params) == 3:
                self.update_by_position(*params)
            else:
                self.update_by_value(*params)
        elif command == "MERGE":
            self.merge(*params)
        elif command == "UNMERGE":
            self.unmerge(*params)
        elif command == "PRINT":
            self.print(*params)

    def update_by_position(self, r, c, value):
        r, c = int(r) - 1, int(c) - 1
        self.table.set(r, c, value)

    def update_by_value(self, value1, value2):
        for r in range(self.table.size):
            for c in range(self.table.size):
                if self.table.get(r, c) == value1:
                    self.table.set(r, c, value2)

    def merge(self, r1, c1, r2, c2):
        self.table.group.merge(int(r1) - 1, int(c1) - 1, int(r2) - 1, int(c2) - 1)

    def unmerge(self, r, c):
        r, c = int(r) - 1, int(c) - 1
        origin_value = self.table.get(r, c)
        self.table.empty(self.table.group.unmerge(r, c))
        self.table.set(r, c, origin_value)

    def print(self, r, c):
        r, c = int(r) - 1, int(c) - 1
        self.result.append(self.table.get(r, c))

def solution(commands):
    answer = []
    table = Table()
    executor = Executor(table)
    group = Group(table.size)
    for command in commands:
        executor.run(command)
    
    return executor.result 
