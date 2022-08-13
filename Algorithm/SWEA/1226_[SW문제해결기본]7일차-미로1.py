from collections import deque

def BFS(start):
    global SIZE
    dir = [[0,1],[0,-1],[1,0],[-1,0]]
    q = deque()
    visited = [[False]*SIZE for _ in range(SIZE)]
    q.append(start)
    while q:
        x,y = q.pop()
        visited[y][x] = True
        if arr[y][x] == 3:
            return True
        for dx,dy in dir:
            px,py = x+dx,y+dy
            if arr[py][px] != 1 and not visited[py][px]:
                q.append((px,py))
    return False

for test in range(10):
    t = int(input())
    SIZE = 16
    arr = [list(map(int, input())) for _ in range(SIZE)]
    start = 0

    for i in range(SIZE):
        for j in range(SIZE):
            if arr[i][j] == 2:
                start = (i,j)
                break
    res = BFS(start)

    if res: print("#{} 1".format(t))
    else: print("#{} 0".format(t))
