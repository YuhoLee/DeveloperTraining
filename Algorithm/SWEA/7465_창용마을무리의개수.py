def DFS(idx):
    for i in range(n+1):
        if relation[idx][i] == 1 and not visited[i]:
            visited[i] = True
            DFS(i)


t = int(input())
for test in range(1,t+1):
    n,m = map(int, input().split())
    arr = []
    for _ in range(m):
        arr += list(map(int, input().split()))
    relation = [[0]*(n+1) for _ in range(n+1)]
    visited = [False]*(n+1)
    for i in range(0,len(arr),2):
        relation[arr[i]][arr[i+1]] = 1
        relation[arr[i+1]][arr[i]] = 1
    arr = list(range(1,n+1))
    res = 0
    for i in range(len(arr)):
        if not visited[arr[i]]:
            visited[arr[i]] = True
            DFS(arr[i])
            res += 1
    print("#{} {}".format(test,res))