from collections import deque

n,l,r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def BFS(bx,by):
    global population,count
    check = []
    q = deque()
    q.append((bx,by))
    visited[by][bx] = True
    while q:
        x,y = q.popleft()
        check.append((x,y))
        population += arr[y][x]
        count += 1
        for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
            px,py = x+dx,y+dy
            if 0 <= px < n and 0 <= py < n:
                if not visited[py][px] and l <= abs(arr[py][px]-arr[y][x]) <= r:
                    q.append((px,py))
                    visited[py][px] = True
    per = population // count
    for x,y in check:
        arr[y][x] = per


day = 0
while True:
    visited = [[False]*n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            population, count = 0,0
            if not visited[i][j]:
                BFS(j,i)
                if count != 1 and not flag:
                    flag = True
                    day += 1
    if not flag: break
print(day)
