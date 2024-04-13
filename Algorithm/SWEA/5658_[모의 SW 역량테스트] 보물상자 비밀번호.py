hexDict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12,
           "D": 13, "E": 14, "F": 15}


def calcDec(hexList):
    global sl
    res = 0
    for i in range(sl):
        res += (pow(16, sl - i - 1) * hexDict[hexList[i]])
    return res


T = int(input())
for tt in range(1, T + 1):
    lock = []
    N, K = tuple(map(int, input().split()))
    cmd = input()
    sl = len(cmd) // 4
    for i in range(4):
        lock.append(list(cmd[i * sl:(i + 1) * sl]))

    caseSet = set()
    for _ in range(sl):
        for i in range(4):
            decVal = calcDec(lock[i])
            caseSet.add(decVal)

        pop0 = lock[0].pop(sl - 1)
        pop1 = lock[1].pop(sl - 1)
        pop2 = lock[2].pop(sl - 1)
        pop3 = lock[3].pop(sl - 1)

        lock[0].insert(0, pop3)
        lock[1].insert(0, pop0)
        lock[2].insert(0, pop1)
        lock[3].insert(0, pop2)

    caseSet = sorted(caseSet,reverse=True)

    print("#{0} {1}".format(tt,caseSet[K-1]))
