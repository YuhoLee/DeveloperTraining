from collections import deque


def bfs():
    global cnt
    q = deque()
    visited = [[False]*m for _ in range(n)]
    state = [[0]*m for _ in range(n)]
    x,y = 0,0
    q.append((x,y))
    visited[y][x] = True
    while q:
        x,y = q.popleft()
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            px,py = x+dx,y+dy
            if not(0 <= px < m and 0 <= py < n): continue
            if arr[py][px] == 1:
                state[py][px] += 1
            if arr[py][px] == 0 and not visited[py][px]:
                visited[py][px] = True
                q.append((px,py))

    for i in range(n):
        for j in range(m):
            if state[i][j] >= 2:
                arr[i][j] = 0
                cnt -= 1


n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = sum([sum(a) for a in arr])
time = 0

while True:
    time += 1
    bfs()
    if cnt == 0: break
print(time)