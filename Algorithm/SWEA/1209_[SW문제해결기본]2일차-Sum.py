for t in range(10):
    test = int(input())
    r_arr = [list(map(int, input().split())) for _ in range(100)]
    # 전치행렬화
    c_arr = list(zip(*r_arr))
    max_num = 0

    for r in r_arr:
        m = sum(r)
        if max_num < m:
            max_num = m

    for c in c_arr:
        m = sum(c)
        if max_num < m:
            max_num = m

    m = sum(r_arr[i][i] for i in range(100))
    if max_num < m:
        max_num = m

    m = sum(r_arr[(i+1)*(-1)][i] for i in range(100))
    if max_num < m:
        max_num = m

    print("#{} {}".format(test, max_num))
