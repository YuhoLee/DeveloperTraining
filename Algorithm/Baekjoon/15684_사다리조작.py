def simulation():
    flag = True
    for i in range(m):
        x,y = i,0
        while y < n:
            if ladder[y][x]:
                if 0 <= x-1 < m and ladder[y][x-1]:
                    x -= 1
                elif 0 <= x+1 < m and ladder[y][x+1]:
                    x += 1
            y += 1
        if i != x:
            flag = False
            break
    return flag


def DFS(x,y,c):
    global c_min
    if c > 3: return
    i = y
    while i < n:
        j = x
        while j < m-1:
            if not ladder[i][j] and not ladder[i][j+1]:
                ladder[i][j], ladder[i][j+1] = 1,1
                if simulation():
                    if c < c_min: c_min = c
                else:
                    DFS(j, i, c + 1)
                ladder[i][j], ladder[i][j+1] = 0,0
            j += 1
        j = 0
        i += 1


n,m,h = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(m)]
ladder = [[0]*m for _ in range(n)]
c_min = float('inf')
for a,b in info:
    ladder[a-1][b-1] = 1
    ladder[a-1][b] = 1

if simulation(): print()
else: DFS(0,0,1)
print(c_min)
