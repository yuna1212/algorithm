"""
시작 시간: 2023-02-14 11:05 AM
소요 시간: 20분
풀이 방법:
"""
def solution(id_list, report, k):
    reported_users = list()
    num_mails = [0]*len(id_list) 
    users_id = dict()

    for i, user in enumerate(id_list):
        users_id[user] = i
        reported_users.append(set())

    for r in report:
        reporter, reported_user = r.split()
        reporter_id, reported_user_id = users_id[reporter], users_id[reported_user]
        reported_users[reported_user_id].add(reporter_id)

    for reported_user_id, reporters in enumerate(reported_users):
        if len(reporters) >= k:
            for reporter_id in reporters:
                num_mails[reporter_id] += 1

    return num_mails 

