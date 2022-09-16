def DFS(idx,c):
    global flag,res
    if c == n:
        flag = True
        res = buff[:]
        return

    if idx == -1:
        for i in range(n):
            visited[i] = True
            buff[c] = screw[i]
            DFS(i, 1)
            if flag: break
            visited[i] = False
            buff[c] = None
    else:
        for i in range(n):
            if not visited[i]:
                end = screw[idx][1]
                s = screw[i][0]
                if end == s:
                    visited[i] = True
                    buff[c] = screw[i]
                    DFS(i, c+1)
                    visited[i] = False
                    buff[c] = None


t = int(input())
for test in range(1,t+1):
    n = int(input())
    arr = list(input().split())
    screw = []
    visited = [False]*n
    for i in range(0,len(arr),2):
        screw.append((arr[i],arr[i+1]))
    buff = [None] * n
    res = []
    flag = False
    DFS(-1,0)
    s = ''
    for a,b in res:
        s += a
        s += ' '
        s += b
        s += ' '
    print("#{} {}".format(test,s))