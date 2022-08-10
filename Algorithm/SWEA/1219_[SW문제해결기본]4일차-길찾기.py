for t in range(1,11):
    test, n = map(int, input().split())
    max_cnt = n
    stack = []
    arrive = []
    isPossible = 0
    arr = list(map(int, input().split()))
    mat = [[0]*(n+1) for _ in range(n+1)]

    for i in range(0,len(arr),2):
        if arr[i+1] == 99:
            arrive.append(arr[i])
            max_cnt -= 1
        else:
            mat[arr[i]][arr[i+1]] = 1
    if arrive != []:
        for i in range(n + 1):
            if mat[0][i] == 1:
                stack.append(i)

        while len(stack) != 0:
            idx = stack.pop(-1)
            if idx in arrive:
                isPossible = 1
                break
            for i in range(n + 1):
                if mat[idx][i] == 1:
                    stack.append(i)
                    mat[idx][i] = 0

    print("#{} {}".format(test, isPossible))
