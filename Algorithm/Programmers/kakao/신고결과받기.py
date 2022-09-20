def solution(id_list, report, k):
    dict_ed = {}
    dict = {}
    for i, user in enumerate(id_list):
        dict[user] = i
        dict_ed[user] = 0
    report = list(set(report))
    for rep in report:
        user, user_ed = rep.split()
        dict_ed[user_ed] += 1

    answer = [0] * len(id_list)
    for rep in report:
        user, user_ed = rep.split()
        if dict_ed[user_ed] >= k:
            answer[dict[user]] += 1

    return answer