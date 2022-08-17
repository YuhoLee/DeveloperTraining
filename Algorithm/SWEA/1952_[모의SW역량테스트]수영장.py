def find(idx, res):
    global result
    if idx > 11:
        if res < result:
            result = res
        return
    find(idx+1,res+candidate[idx])
    find(idx+3,res+fee[2])

t = int(input())
for test in range(1,t+1):
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    candidate = [0] * 12

    # (1개월 fee / 1일 fee)가 일수보다 작으면 1개월치가 나음
    # 3개월이 1개월 fee의 합보다 작으면 3개월치가 나음
    # 3개월이 1일 및 1개월 조합들의 합보다 작으면 3개월치가 나음
    for i in range(12):
        candidate[i] = plan[i] * fee[0]
        if candidate[i] > fee[1]:
            candidate[i] = fee[1]
    result = sum(candidate)
    find(0,0)
    if result > fee[3]:
        result = fee[3]
    print("#{} {}".format(test, result))
