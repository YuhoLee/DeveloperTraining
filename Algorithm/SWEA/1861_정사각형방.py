import sys
sys.setrecursionlimit(1000000)

def DFS(x,y,c):
    flag = True
    buff = []
    for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
        px,py = x+dx,y+dy
        if 0 <= px < n and 0 <= py < n:
            if arr[y][x]+1 == arr[py][px] and not visited[py][px]:
                flag = False
                visited[py][px] = True
                buff.append(DFS(px,py,c+1))
                visited[py][px] = False
    if flag:
        return c
    else: return max(buff)


t = int(input())
for test in range(1,t+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    sorted_arr = [0] * (n*n+1)
    for i in range(n):
        for j in range(n):
            sorted_arr[arr[i][j]] = (j,i)
    m = 0
    start = 0
    visited = [[False]*n for _ in range(n)]
    idx = 1
    while idx < n*n+1:
        x,y = sorted_arr[idx]
        res = DFS(x,y,1)
        if m < res:
            m = res
            start = arr[y][x]
        idx += res

    print("#{} {} {}".format(test,start,m))