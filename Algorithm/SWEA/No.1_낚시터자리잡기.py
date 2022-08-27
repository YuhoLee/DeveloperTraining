from itertools import permutations

def DFS(gg, arr, stage):
    global min_count
    if stage == 3:
        s = sum(arr)
        if min_count > s: min_count = s
        return
    pos, count = gate[gg[stage]]
    if arr[pos] == 0:
        arr[pos] = 1
        count -= 1
    pp = 2
    left, right = pos-1, pos+1
    flag = False
    while count > 0:
        if 0 <= left < n and 0 <= right < n:
            if count == 1 and arr[left] == 0 and arr[right] == 0:
                flag = True
                break

        if 0 <= left < n:
            if arr[left] == 0:
                arr[left] = pp
                count -= 1

        if count == 0: break

        if 0 <= right < n:
            if arr[right] == 0:
                arr[right] = pp
                count -= 1
        left -= 1
        right += 1
        pp += 1

    if flag:
        arr[left] = pp
        DFS(gg,arr[:],stage+1)
        arr[left] = 0
        arr[right] = pp
        DFS(gg,arr[:],stage+1)
    else:
        DFS(gg,arr[:],stage+1)

t = int(input())
for test in range(1,t+1):
    n = int(input())
    gate = []
    for _ in range(3):
        p, c = map(int, input().split())
        gate.append((p-1,c))
    min_count = float('inf')
    for gg in permutations(range(3),3):
        DFS(gg, [0]*n, 0)
    print("#{} {}".format(test, min_count))