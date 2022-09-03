def work():
    for i in range(len(arr)):
        mm = max(arr[i]) + 1
        counter = [0] * mm
        for j in range(len(arr[i])):
            counter[arr[i][j]] += 1
        buff = []
        for j in range(1, max(counter) + 1):
            for idx in range(1, mm):
                if counter[idx] == j:
                    buff.append(idx)
                    buff.append(j)
        arr[i] = buff
    l_max = max([len(ar) for ar in arr])
    for ar in arr:
        ar += ([0] * (l_max-len(ar)))


r,c,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
cnt = 0
flag = False
while cnt <= 100:
    rl = len(arr)
    cl = len(arr[0])
    if rl >= r and cl >= c and arr[r-1][c-1] == k:
        flag = True
        break

    if rl >= cl:
        work()
    else:
        arr = list(map(list, zip(*arr)))
        work()
        arr = list(map(list, zip(*arr)))
    cnt += 1

if flag: print(cnt)
else: print(-1)