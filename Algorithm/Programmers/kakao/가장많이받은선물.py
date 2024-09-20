def solution(friends, gifts):
    # 선물 더 많이 준 사람이 다음달에 선물을 하나 받음.
    # 주고 받은 기록이 없거나 주고 받은 수가 같으면 선물지수가 더 큰 사람이 받음.
    # 선물 지수는 이번달까지 자신이 친구들에게 준 선물의 수에서 받은 선물 수를 뺀 값
    # 선물 지수도 같으면 선물을 주고받지 않음.

    fl = len(friends)
    gift_table = [[0] * fl for _ in range(fl)]

    fidx = {}
    for idx, friend in enumerate(friends):
        fidx[friend] = idx

    for gift in gifts:
        (giver, getter) = gift.split(' ')
        gift_table[fidx[giver]][fidx[getter]] += 1

    ng = [0] * fl
    for i in range(fl):
        for j in range(i+1, fl):
            t1, t2 = fidx[friends[i]], fidx[friends[j]]
            if gift_table[t1][t2] > gift_table[t2][t1]:
                ng[t1] += 1
            elif gift_table[t1][t2] < gift_table[t2][t1]:
                ng[t2] += 1
            else:
                t1Score = sum(gift_table[t1]) - sum([tt[t1] for tt in gift_table])
                t2Score = sum(gift_table[t2]) - sum([tt[t2] for tt in gift_table])

                if t1Score > t2Score:
                    ng[t1] += 1
                elif t1Score < t2Score:
                    ng[t2] += 1

    print(max(ng))


# solution(["muzi", "ryan", "frodo", "neo"],
#          ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])
#
# solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"])
solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"])