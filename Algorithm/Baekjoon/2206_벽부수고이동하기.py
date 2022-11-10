from collections import deque


def bfs():
    global n,m,res
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        x,y,c = q.popleft()
        if x == m-1 and y == n-1:
            return visited[y][x][c]
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            px,py = x+dx,y+dy
            if not(0 <= px < m and 0 <= py < n): continue
            if arr[py][px] == 1 and c == 0:
                visited[py][px][1] = visited[y][x][0] + 1
                q.append((px,py,1))
            elif arr[py][px] == 0 and visited[py][px][c] == 0:
                visited[py][px][c] = visited[y][x][c] + 1
                q.append((px,py,c))
    return float('inf')


# init
n,m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
res = float('inf')
res = bfs()
if res != float('inf'): print(res)
else: print(-1)