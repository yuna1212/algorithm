import random
import sys
class TestCase:
    def __init__(self, how_many, min_value, max_value, allow_duplication=True):
        self.how_many, self.min_value, self.max_value = how_many, min_value, max_value
        self.test_cases = []
        if allow_duplication:
            for _ in range(how_many):
                self.test_cases.append(random.randrange(min_value, max_value+1))
        else:
            if max_value - min_value < how_many:
                print("만들 개수보다 최대 최소값 범위가 더 작습니다.")
                sys.exit(1)
                
            for _ in range(how_many):
                random_number = random.randrange(min_value, max_value+1)
                while random_number in self.test_cases:
                    random_number = random.randrange(min_value, max_value+1)
                self.test_cases.append(random_number)
    
    def __repr__(self):
        return f'개수: {self.how_many}, 최솟값: {self.min_value}, 최댓값: {self.max_value}'
    
    def print_one_line(self):
        print(self)
        for case in self.test_cases:
            print(case, end=' ')
    
    def print_many_lines(self, number_of_values_in_a_line):
        print(self)
        for i in range(self.how_many // number_of_values_in_a_line):
            for j in range(i*number_of_values_in_a_line, (i+1)*number_of_values_in_a_line):
                print(self.test_cases[j], end=" ")
            print()
"""
    test_case = TestCase(how_many=30, min_value=1, max_value=10)
    test_case.print_one_line()
"""
test_case = TestCase(how_many=100, min_value=1, max_value=20)
test_case.print_many_lines(2)
print("------------")
print(max(test_case.test_cases))
print(min(test_case.test_cases))