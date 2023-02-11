"""
시작 시간: 2023-02-12 12:49 AM
소요 시간: 2시간 20분
풀이 방법:
"""
class User:
    def __init__(self, ratio, limit):
        self.ratio = ratio
        self.limit = limit
        self.bill = 0
        self.is_subscribed = False

def print_users():
    global USERS
    print('-------------------')
    print('id\t구매액\t가입여부')
    for i, user in enumerate(USERS):
        print(f'{i+1}\t{user.bill}\t{user.is_subscribed}')

def search(emoticon_index, ratio, amount_selling, num_of_subscriber):
    global EMOTICONS, USERS
    if emoticon_index == len(EMOTICONS): 
        return num_of_subscriber, amount_selling

    cost = EMOTICONS[emoticon_index]*(100-ratio)//100
    buyers = set() 
    subscribers = set()

    for i, user in enumerate(USERS):
        if user.is_subscribed or user.ratio > ratio: continue

        amount_selling -= user.bill
        if user.bill + cost >= user.limit:
            num_of_subscriber += 1
            user.is_subscribed = True
            subscribers.add(i)
        else:
            user.bill += cost
            buyers.add(i) 

    print('구독자, 팔린 수', num_of_subscriber, amount_selling)
    
    next_index = emoticon_index+1
    for next_ratio in (10, 20, 30, 40):
        next_amount_selling, next_num_of_subscriber = search(next_index, next_ratio, amount_selling, num_of_subscriber)
        if next_num_of_subscriber > num_of_subscriber:
            num_of_subscriber = next_num_of_subscriber
            amount_selling = next_amount_selling
        elif next_num_of_subscriber == num_of_subscriber:
            amount_selling = max(amount_selling, next_amount_selling)

    for i, user in enumerate(USERS):
        if i in buyers:
            user.bill -= cost
        elif i in subscribers:
            user.is_subscribed = False
    
    return num_of_subscriber, amount_selling


def solution(users, emoticons):
    global EMOTICONS, USERS
    EMOTICONS = emoticons
    USERS = [ User(ratio, limit) for ratio, limit in users ] 

    answer = [0, 0]
    for ratio in (10, 20, 30, 40):
        num_of_subscriber, amount_selling = search(0, ratio, 0, 0)
        if answer[0] < num_of_subscriber:
            answer[0] = num_of_subscriber
            answer[1] = amount_selling

        elif answer[0] == num_of_subscriber:
            answer[1] = max(answer[1], amount_selling)
        
    print('answer', answer)
    print_users()
    return answer

solution([[40, 10000], [25, 10000]], [7000, 9000])
