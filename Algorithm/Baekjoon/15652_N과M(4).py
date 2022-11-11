def dfs(num,c):
    if c == m:
        print(' '.join(list(map(str, arr))))
        return

    for k in range(num,n+1):
        arr.append(k)
        dfs(k,c+1)
        arr.pop(-1)


n,m = map(int, input().split())
arr = []
dfs(1,0)