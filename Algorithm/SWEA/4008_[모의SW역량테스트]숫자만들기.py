def calc(idx, res, c1, c2, c3, c4):
    global min_num, max_num
    if idx >= n:
        if res < min_num: min_num = res
        if res > max_num: max_num = res
        return
    if c1 != 0:
        calc(idx+1, res+num[idx], c1-1, c2, c3, c4)
    if c2 != 0:
        calc(idx+1, res-num[idx], c1, c2-1, c3, c4)
    if c3 != 0:
        calc(idx+1, res*num[idx], c1, c2, c3-1, c4)
    if c4 != 0:
        if res < 0:
            calc(idx+1, ((-1)*res)//num[idx]*(-1), c1, c2, c3, c4-1)
        else: calc(idx+1, res//num[idx], c1, c2, c3, c4-1)


t = int(input())
for test in range(1,t+1):
    n = int(input())
    oper = list(map(int, input().split()))
    num = list(map(int, input().split()))
    min_num, max_num = float('inf'), float('-inf')

    calc(1,num[0], oper[0], oper[1], oper[2], oper[3])
    print("#{} {}".format(test, max_num - min_num))