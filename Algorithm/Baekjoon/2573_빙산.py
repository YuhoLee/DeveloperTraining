from collections import deque
dir = [[0,-1],[0,1],[-1,0],[1,0]]

def BFS(arr):
    global h,w
    q = deque()
    buff = []
    for a in arr:
        buff.append(a[:])
    visited = [[False]*w for _ in range(h)]
    count = 0
    while True:
        found = False
        for i in range(h):
            for j in range(w):
                if arr[i][j] != 0 and not visited[i][j]:
                    q.append((j,i))
                    visited[i][j] = True
                    found = True
                    break
            if found: break
        if not found: break
        while q:
            x,y = q.pop()
            for i in range(4):
                dx = x + dir[i][0]
                dy = y + dir[i][1]
                if 0 <= dx < w and 0 <= dy < h:
                    if arr[y][x] != 0:
                        if arr[dy][dx] == 0 and buff[y][x] > 0:
                            buff[y][x] -= 1
                    if not visited[dy][dx] and arr[dy][dx] != 0:
                        q.append((dx,dy))
                        visited[dy][dx] = True
        count += 1
    return buff,count

h,w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
res = 0
while True:
    arr, c = BFS(arr)
    if c == 0:
        res = 0
        break
    if c != 1:
        break
    else: res += 1
print(res)


