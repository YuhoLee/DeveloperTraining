from itertools import combinations
from collections import deque

dir = [[0,-1],[0,1],[-1,0],[1,0]]


def BFS(c):
    global min_val
    q = deque()
    visited = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                visited[i][j] = float('-inf')

    for vv in c:
        q.append(vv)
        visited[vv[1]][vv[0]] = 0
    while q:
        x,y = q.popleft()
        for dx,dy in dir:
            px,py = x+dx,y+dy
            if not(0 <= px < n and 0 <= py < n): continue
            if visited[py][px] == -1 and (arr[py][px] == 0 or arr[py][px] == -2):
                q.append((px,py))
                visited[py][px] = visited[y][x] + 1
    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                flag = True
                break
            if arr[i][j] == -2: visited[i][j] = float('-inf')
    if not flag:
        mm = max([max(v) for v in visited])
        if min_val > mm:
            min_val = mm


n, v = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2: virus.append((j,i))
vc = len(virus)

min_val = float('inf')
case = combinations(virus,v)
for c in case:
    no = []
    for i in range(vc):
        if virus[i] not in c:
            arr[virus[i][1]][virus[i][0]] = -2
            no.append(virus[i])
    BFS(c)
    for nv in no:
        arr[nv[1]][nv[0]] = 2
if min_val != float('inf'):
    print(min_val)
else: print(-1)