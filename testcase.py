import random
class TestCase:
    def __init__(self, how_many, min_value, max_value):
        self.how_many, self.min_value, self.max_value = how_many, min_value, max_value
        self.test_cases = []
        for _ in range(how_many):
            self.test_cases.append(random.randrange(min_value, max_value+1))
    
    def print_one_line(self):
        print(f'개수: {self.how_many}, 최솟값: {self.min_value}, 최댓값: {self.max_value}')
        for case in self.test_cases:
            print(case, end=' ')

"""
    test_case = TestCase(how_many=30, min_value=1, max_value=10)
    test_case.print_one_line()
"""