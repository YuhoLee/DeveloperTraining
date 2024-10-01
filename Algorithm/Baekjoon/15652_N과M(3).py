n,m = tuple(map(int, input().split()))
arr = []
res = []


def dfs(count: int):
    global n,m
    if count == m :
        print(' '.join(arr))
        return

    for i in range(1, n+1):
        arr.append(str(i))
        dfs(count+1)
        arr.pop()


dfs(0)