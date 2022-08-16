from itertools import combinations
from collections import deque

h,w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

def BFS():
    q = deque()
    buff = []
    for a in arr:
        buff.append(a[:])
    visited = [[False]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if buff[i][j] == 0: cnt += 1
            if buff[i][j] == 2:
                q.append((j,i))
                visited[i][j] = True
    while q:
        x,y = q.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            px,py = x+dx,y+dy
            if 0 <= px < w and 0 <= py < h:
                if buff[py][px] == 0 and not visited[py][px]:
                    q.append((px,py))
                    visited[py][px] = True
                    buff[py][px] = 2
                    cnt -= 1
    return cnt

l = []
res = 0
for i in range(h):
    for j in range(w):
      l.append((j,i))
com = combinations(l,3)
for c in com:
    x1,y1 = c[0][0],c[0][1]
    x2,y2 = c[1][0],c[1][1]
    x3,y3 = c[2][0],c[2][1]
    if arr[y1][x1] == 0 and arr[y2][x2] == 0 and arr[y3][x3] == 0:
        arr[y1][x1], arr[y2][x2], arr[y3][x3] = 1,1,1
        res = max(res,BFS())
        arr[y1][x1], arr[y2][x2], arr[y3][x3] = 0,0,0
print(res)