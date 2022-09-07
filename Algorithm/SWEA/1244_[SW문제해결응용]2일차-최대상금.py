def DFS(i,change):
    global l, max_num,cc
    #
    if i == l-1 or change == 0:
        num = int(''.join(list(map(str, arr))))
        if max_num < num:
            max_num = num
            cc = change
        return
    mm = max(arr[i:])
    if arr[i] != mm:
        mm_list = []
        s = ''.join(list(map(str, arr)))
        while True:
            idx = s.rfind(str(mm))
            if idx != -1:
                mm_list.append(idx)
                s = s[:idx]
            else: break
        for index in mm_list:
            if index > i:
                tmp = arr[index]
                arr[index] = arr[i]
                arr[i] = tmp
                DFS(i+1,change-1)
                tmp = arr[index]
                arr[index] = arr[i]
                arr[i] = tmp
    else:
        DFS(i+1,change)


t = int(input())
for test in range(1,t+1):
    inp = input().split(' ')
    arr = list(map(int, list(inp[0])))
    cc = int(inp[1])
    l = len(arr)
    max_num = 0
    DFS(0,cc)

    # 숫자가 같은 값이 붙어 있는 경우
    # ->
    flag = False
    max_num = list(str(max_num))
    for i in range(l-1):
        if max_num[i] == max_num[i+1]:
            flag = True
            break
    if not flag:
        if cc % 2 == 1:
            tmp = max_num[-2]
            max_num[-2] = max_num[-1]
            max_num[-1] = tmp
    max_num = ''.join(max_num)
    print("#{} {}".format(test, max_num))