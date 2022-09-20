from collections import deque

tunnel = [[],
          [[0,1],[1,0],[0,-1],[-1,0]],
          [[0,1],[0,-1]],
          [[1,0],[-1,0]],
          [[1,0],[0,-1]],
          [[1,0],[0,1]],
          [[-1,0],[0,1]],
          [[-1,0],[0,-1]]]


def BFS(point):
    global l
    q = deque()
    visited = [[False]*m for _ in range(n)]
    q.append((point[0],point[1],1))
    visited[point[1]][point[0]] = True
    total = 1
    while q:
        x,y,cc = q.popleft()
        if cc >= l: break
        d = arr[y][x]
        for dx,dy in tunnel[d]:
            px,py = x+dx,y+dy
            if not (0 <= px < m and 0 <= py < n): continue
            if arr[py][px] > 0 and not visited[py][px]:
                dd = arr[py][px]
                flag = False
                for ddx,ddy in tunnel[dd]:
                    ppx,ppy = px+ddx,py+ddy
                    if ppx == x and ppy == y:
                        flag = True
                        break
                if flag:
                    visited[py][px] = True
                    q.append((px,py,cc+1))
                    total += 1
    return total


t = int(input())
for test in range(1, t+1):
    n,m,r,c,l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    if l == 1:
        res = 1
    elif l > 1:
        res = BFS((c,r))

    print("#{} {} ".format(test,res))