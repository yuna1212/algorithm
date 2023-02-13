"""
시작 시간: 2023-02-13 12:17 PM
소요 시간: 1시간 30분
풀이 방법: brute force. 유저 수는 최대 100, 할인율에 따른 이모티콘 가격 경우의 수는 16K => 무식하게 풀어도 1.6M 경우만 살피기에 충분
"""
def get_result_by(discount_ratio):
    num_subscribers = 0
    benefit = 0
    for (user_ratio, user_limit) in USERS:
        bill = 0
        for i, emoticon in enumerate(EMOTICONS):
            if discount_ratio[i] >= user_ratio:
                bill += emoticon*(100-discount_ratio[i])//100

        if bill >= user_limit:
            num_subscribers += 1
        else:
            benefit += bill
        
    return num_subscribers, benefit

USERS = [[40, 10000], [25, 10000]]
EMOTICONS = 	[7000, 9000]


def get_optimal_result(discount_ratio, idx):
    optimal_num_subscribers, optimal_benefit = get_result_by(discount_ratio)

    if idx < len(EMOTICONS):
        for ratio in (10, 20, 30, 40):
            discount_ratio[idx] = ratio
            num_subscribers, benefit = get_optimal_result(discount_ratio, idx+1)

            if optimal_num_subscribers < num_subscribers:
                optimal_num_subscribers = num_subscribers
                optimal_benefit = benefit

            elif optimal_num_subscribers == num_subscribers:
                optimal_benefit = max(optimal_benefit, benefit)

        discount_ratio[idx] = 10

    return optimal_num_subscribers, optimal_benefit

            
def solution(users, emoticons):
    global USERS, EMOTICONS
    USERS, EMOTICONS = users, emoticons

    return get_optimal_result([10]*len(EMOTICONS), 0) 

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
