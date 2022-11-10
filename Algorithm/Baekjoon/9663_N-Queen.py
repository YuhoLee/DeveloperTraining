def calc_cross(x,y):
    for dx,dy in [[-1,-1],[1,-1]]:
        px,py = x,y
        while True:
            px,py = px+dx,py+dy
            if not(0 <= px < n and 0 <= py < n): break
            if arr[py][px] == 1: return False
    return True


def dfs(x,y,c):
    global res
    if y >= n:
        if c == n:
            res += 1
        return
    if x >= n:
        dfs(0,y+1,c)
    else:
        for i in range(n):
            if col[i] == 0 and calc_cross(i,y):
                arr[y][i] = 1
                col[i] = 1
                dfs(0,y+1,c+1)
                col[i] = 0
                arr[y][i] = 0


n = int(input())
arr = [[0]*n for _ in range(n)]
col = [0] * n
res = 0
dfs(0,0,0)
print(res)