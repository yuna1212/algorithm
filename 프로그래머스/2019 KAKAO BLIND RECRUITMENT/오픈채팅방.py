"""
시작 시간: 2022년 5월 18일 오후 9시 45분
소요 시간: 20분
풀이 방법:
    dictionary 사용
"""
ENTER = 1
LEAVE = 2
CHANGE = 3
USERS_NICKNAME = {}

def parser(a_record):
    splited_record = list(a_record.split())
    if len(splited_record) == 2:
        return LEAVE, splited_record[1]
    elif splited_record[0][0] == "E":
        return ENTER, splited_record[1], splited_record[2]
    else:
        return CHANGE, splited_record[1], splited_record[2]
def operate(command):
    if len(command) == 2:
        return
    _, user_id, nickname = command
    USERS_NICKNAME[user_id] = nickname
def get_result_string(command):
    if len(command) == 2:
        user_id = command[1]
        return USERS_NICKNAME[user_id]+"님이 나갔습니다."
    command, user_id, _ = command
    if command == ENTER:
        return USERS_NICKNAME[user_id]+"님이 들어왔습니다."
    return None

def solution(record):
    answer = []
    commands = []
    for a_record in record:
        command = parser(a_record)
        operate(command)
        commands.append(command)
    for command in commands:
        result = get_result_string(command)
        if result:
            answer.append(result)
    return answer