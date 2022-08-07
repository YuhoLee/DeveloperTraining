testcase = int(input())
for test in range(testcase):
    # l분 이상 u분 이하 해야함 / x분 운동
    l,u,x = tuple(map(int, input().split(' ')))
    res = 0

    # 더 많은 운동을 하는 경우
    if x > u: res = -1
    # 운동을 더 적게 하는 경우 
    # -> 최소운동량 - 현재 운동량 = 부족한 운동량
    elif x < l: res = l-x;
    # 적정 운동량
    else: res = 0
    print("#{} {}".format(test+1,res))