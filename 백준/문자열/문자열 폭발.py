"""
시작 시간: 2022년 5월 11일 오전 12시 45분
소요 시간: 45분
풀이 방법:
    kmp 알고리즘
    시간초과..
"""
def solution(string, bomb):
    bomb_size = len(bomb)
    bomb_pattern_table = make_KMP_table(bomb)
    bomb_positions = kmp(string, bomb, bomb_pattern_table)
    while bomb_positions:
        string = explode(string, bomb_positions, bomb_size)
        bomb_positions = kmp(string, bomb, bomb_pattern_table)
    if string:
        return string
    return "FRULA"
def explode(string, bomb_positions, bomb_size):
    last_bomb_position = bomb_positions[0]
    new_string = string[:last_bomb_position]
    for i in range(1, len(bomb_positions)):
        bomb_position = bomb_positions[i]
        new_string += string[last_bomb_position+bomb_size:bomb_position]
        last_bomb_position = bomb_position
    new_string += string[last_bomb_position+bomb_size:]
    return new_string
    
def make_KMP_table(pattern):
    pattern_size = len(pattern)
    table = [0] * pattern_size
    affix_length = 0
    for i in range(1, pattern_size):
        while affix_length > 0 and pattern[i] != pattern[affix_length]:
            affix_length = table[affix_length - 1]
        if pattern[i] == pattern[affix_length]:
            affix_length += 1
            table[i] = affix_length
    return table
def kmp(sentence, pattern, pattern_table):
    ret = []
    sentence_size = len(sentence)
    pattern_size = len(pattern)
    affix_length = 0
    for i in range(0, sentence_size):
        while affix_length > 0 and sentence[i] != pattern[affix_length]:
            affix_length = pattern_table[affix_length-1]
        if sentence[i] == pattern[affix_length]:
            if affix_length == pattern_size - 1:
                ret.append(i - pattern_size + 1)
                affix_length = pattern_table[affix_length]
            else:
                affix_length += 1
    return ret

# 데이터 입력
sentence = input()
bomb = input()
print(solution(sentence, bomb))