def dfs(c):
    if c == m:
        print(' '.join(list(map(str, num))))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            num.append(arr[i])
            dfs(c+1)
            num.pop(-1)
            visited[i] = False


n,m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
num = []
visited = [False] * n
dfs(0)