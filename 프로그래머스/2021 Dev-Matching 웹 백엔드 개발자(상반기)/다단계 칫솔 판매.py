"""
시작 시간: 2022년 6월 10일 오전 10시 48분
소요 시간: 1시간
풀이 방법:
    
""" 
def get_mine_and_superiors_profit(total_profit):
    superiors = int(total_profit*0.1)
    return total_profit - superiors, superiors
        
def allocate_profit(seller, superior_of, total_profit, profit_of):
    stack = [(seller, total_profit)]
    while stack:
        member, total_profit = stack.pop()
        member_profit, superior_profit = get_mine_and_superiors_profit(total_profit)
        
        superior = superior_of[member]
        
        if superior > -1: # 추천인이 있다면    
            if superior_profit > 0: # 추천인의 이익이 1 이상이라면
                stack.append((superior, superior_profit))
        
        profit_of[member] += member_profit
    return

def solution(enroll, referral, seller, amount):
    # 직원 이름으로 id 찾기
    enroll_id = dict()
    for i in range(len(enroll)):
        enroll_id[enroll[i]] = i
        
    # 직원 각각의 이득 저장, 인덱스는 직원의 id를 의미
    profit_of = [0] * len(enroll)
    
    # 직속 상사의 id
    superior_of = [-1] * len(enroll)
    for i in range(len(enroll)):
        if referral[i] != "-":
            superior_of[i] = enroll_id[referral[i]]
    
    for i in range(len(seller)):
        total_profit = amount[i]*100
        allocate_profit(enroll_id[seller[i]], superior_of, total_profit, profit_of)
    return profit_of

print(solution(	["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))