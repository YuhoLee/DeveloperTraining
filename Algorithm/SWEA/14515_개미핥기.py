dir = [[-1,0],[0,-1],[1,0],[0,1]]


def dfs(x,y,length,c):
    global holeCount, res, visited, cc
    # print("x,y: ({},{}) / length: {} / c: {}".format(x,y,length,c))
    cc += 1
    if c > holeCount:
        if res < length:
            res = length
        return

    nx,ny = x+1,y
    if nx == m:
        nx = 0
        ny += 1

    for i in range(4):
        fpx,fpy = x+dir[i][0], y+dir[i][1]
        if not (0 <= fpx < m and 0 <= fpy < n): continue
        for j in range(4):
            spx,spy = x+dir[j][0], y+dir[j][1]
            if not (0 <= spx < m and 0 <= spy < n): continue
            print("point: ({},{}) / first: ({},{}) / second: ({},{})".format(x,y,fpx,fpy,spx,spy))
            # print(x,y,c)
            fv,sv = arr[y][x]

            # 첫번째 개미핥기만 혀를 내미는 경우
            if graph[x][fpx][y][fpy] >= fv:
                graph[x][fpx][y][fpy] -= fv
                dfs(nx,ny,length + fv, c+1)
                graph[x][fpx][y][fpy] += fv

            # 두번째 개미핥기만 혀를 내미는 경우
            if graph[x][spx][y][spy] >= sv:
                graph[x][spx][y][spy] -= sv
                dfs(nx, ny, length + sv, c + 1)
                graph[x][spx][y][spy] += sv

            # 두 개미핥기가 모두 혀를 내미는 경우
            if i != j:
                if graph[x][fpx][y][fpy] >= fv and graph[x][spx][y][spy] >= sv:
                    graph[x][fpx][y][fpy] -= fv
                    graph[x][spx][y][spy] -= sv
                    dfs(nx, ny, length + fv + sv, c + 1)
                    graph[x][fpx][y][fpy] += fv
                    graph[x][spx][y][spy] += sv

            # 둘 다 혀를 내밀지 않는 경우
            dfs(nx, ny, length, c + 1)


t = int(input())
for test in range(1,t+1):
    n = int(input())
    wl = int(input())
    arr = []
    cc = 0
    for _ in range(n):
        row = list(map(int, input().split()))
        buff = []
        for i in range(0,len(row),2):
            buff.append([row[i],row[i+1]])
        arr.append(buff)
    m = len(arr[0])
    holeCount = n*m
    graph = [[[[0]*n for _ in range(n)] for _ in range(m)] for _ in range(m)]
    for i in range(n-1):
        hl = int(input())
        for j in range(m):
            graph[j][j][i][i+1] = hl
            graph[j][j][i+1][i] = hl
    for i in range(m-1):
        for j in range(n):
            graph[i][i+1][j][j] = wl
            graph[i+1][i][j][j] = wl

    visited = [[False]*m for _ in range(n)]

    res = 0
    dfs(0,0,0,1)
    print("#{} {}".format(test,res))



