from collections import deque

dice = [[0,2,0],
        [4,1,3],
        [0,5,0],
        [0,6,0]]
dir = [[1,0],[0,1],[-1,0],[0,-1]]


def move(d):
    tmp = dice[3][1]
    if d == 0:
        dice[3][1] = dice[1].pop(-1)
        dice[1].insert(0,tmp)
    elif d == 1:
        tmp = dice[3][1]
        for i in range(2,-1,-1):
            dice[i+1][1] = dice[i][1]
        dice[0][1] = tmp
    elif d == 2:
        dice[3][1] = dice[1].pop(0)
        dice[1].append(tmp)
    elif d == 3:
        tmp = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i+1][1]
        dice[3][1] = tmp


def get_score(x,y,target):
    visited = [[False]*m for _ in range(n)]
    q = deque()
    cnt = 1
    q.append((x,y))
    visited[y][x] = True
    while q:
        x,y = q.popleft()
        for dx,dy in dir:
            px,py = x+dx,y+dy
            if not(0 <= px < m and 0 <= py < n):
                continue
            if not visited[py][px] and arr[py][px] == target:
                visited[py][px] = True
                cnt += 1
                q.append((px,py))

    return cnt*target


n,m,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
d = 0
x,y = 0,0
res = 0
for _ in range(k):
    dx,dy = dir[d]
    x,y = x+dx,y+dy
    if not(0 <= x < m and 0 <= y < n):
        d = (d+2) % 4
        dx, dy = dir[d]
        x,y = x+2*dx, y+2*dy
    move(d)
    res += get_score(x,y,arr[y][x])
    bottom = dice[3][1]
    curr = arr[y][x]
    if bottom > curr:
        d = (d+1) % 4
    elif bottom < curr:
        d = (d-1) % 4
print(res)