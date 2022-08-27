def shuffle(left, right, x):
    global n, p
    res = [0] * n
    lp,rp = 0,0
    for i in range(p-1,-1,-1):
        dx = x-lp
        if dx > p: dx = p
        elif dx < 0: dx = 0
        res[i+dx] = left[i]
        lp += 1
    for i in range(p):
        dx = x-rp
        if dx > p: dx = p
        elif dx < 0:
            dx = 0
        res[i+p-dx] = right[i]
        rp += 1
    return res


def DFS(arr, count):
    global min_shuffle, n, p
    if count > 5:
        return
    if arr == sorted_arr or arr == reverse_sorted_arr:
        if min_shuffle > count: min_shuffle = count
    for x in range(1, n):
        buff = shuffle(arr[:p], arr[p:], x)
        DFS(buff[:], count + 1)


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    p = n // 2
    arr = list(map(int, input().split()))
    min_shuffle = float('inf')
    sorted_arr = sorted(arr)
    reverse_sorted_arr = sorted(arr, reverse=True)
    DFS(arr[:], 0)
    if min_shuffle == float('inf'): print("#{} {}".format(test,-1))
    else: print("#{} {}".format(test,min_shuffle))