"""
시작 시간: 2023-02-16 04:02 PM
소요 시간: 2시간
풀이 방법:
    - 문제 조건에, merge 할 때 두 셀 중 하나가 값이 없다면, 있는걸 우선으로 하여 가진다고 명시됨..
    - 조건 잘 읽어보기ㅜㅜ
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

    def union(self, r1, c1, r2, c2):
        r1, c1 = self.find(r1, c1)
        r2, c2 = self.find(r2, c2)
        if (r1, c1) == (r2, c2): return
        if self.heights[r1][c1] < self.heights[r2][c2]:
            r1, r2 = r2, r1
            c1, c2 = c2, c1

        self.parent[r2][c2] = r1, c1

        if self.heights[r1][c1] == self.heights[r2][c2]:
            self.heights[r1][c1] += 1

    def ununion(self, r, c):
        cells = []
        r, c = self.find(r, c)
        for x in range(self.table_size):
            for y in range(self.table_size):
                if self.find(x, y) == (r, c):
                    cells.append((x, y))

        for r, c in cells:
            self.parent[r][c] = (r, c)
            self.heights[r][c] = 0

        return cells

class Table:
    def __init__(self):
        self.size = 50
        self.table = [[ "EMPTY" for _ in range(self.size) ] for _ in range(self.size) ]
        self.group = Group(self.size)

    def empty(self, positions):
        for r, c in positions:
            self.table[r][c] = "EMPTY"

    def get(self, r, c):
        r, c = self.group.find(r, c)
        return self.table[r][c]

    def set(self, r, c, value):
        r, c = self.group.find(r, c)
        self.table[r][c] = value

class Editor:
    def __init__(self):
        self.table = Table()
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
        r, c = self.convert(r, c)
        self.table.set(r, c, value)

    def update_by_value(self, value1, value2):
        for r in range(self.table.size):
            for c in range(self.table.size):
                if self.table.get(r, c) == value1:
                    self.table.set(r, c, value2)

    def merge(self, r1, c1, r2, c2):
        r1, c1 = self.convert(r1, c1)
        r2, c2 = self.convert(r2, c2)
        value = self.table.get(r1, c1)
        if value == "EMPTY":
            value = self.table.get(r2, c2)
        self.table.group.union(r1, c1, r2, c2)
        self.table.set(r1, c1, value)

    def unmerge(self, r, c):
        r, c = self.convert(r, c)
        value = self.table.get(r, c)
        cells = self.table.group.ununion(r, c)
        self.table.empty(cells)
        self.table.set(r, c, value)

    def print(self, r, c):
        r, c = self.convert(r, c)
        self.result.append(self.table.get(r, c))

    def convert(self, r, c):
        r, c = int(r) - 1, int(c) - 1
        return r, c

def solution(commands):
    editor = Editor()

    for command in commands:
        editor.run(command)

    return editor.result
