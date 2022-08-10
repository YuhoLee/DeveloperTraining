for test in range(1, 11):
    stack = []
    v, e = map(int, input().split())
    arr = list(map(int, input().split()))
    mat = [[0] * (v+1) for _ in range(v+1)]
    for i in range(0,len(arr)-1,2):
        mat[arr[i]][arr[i+1]] = 1

    c_mat = list(map(list, zip(*mat)))
    order_list = []
    for i,m in enumerate(c_mat):
        if sum(m) == 0:
            stack.append(i)

    while len(stack) != 0:
        n = stack.pop(-1)
        order_list.append(n)
        for i in range(v+1):
            if c_mat[i][n] == 1:
                c_mat[i][n] = 0
                if sum(c_mat[i]) == 0:
                    stack.append(i)

    order_list.pop(-1)
    print("#{} {}".format(test, ' '.join(map(str, order_list))))