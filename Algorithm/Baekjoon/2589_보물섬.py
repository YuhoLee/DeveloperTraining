from collections import deque
dir = [[0,1],[0,-1],[1,0],[-1,0]]
def BFS(px,py):
    global h,w
    q = deque()
    q.append((px,py,0))
    visited = [[False] * w for _ in range(h)]
    visited[py][px] = True
    countList = []
    while q:
        x,y,c = q.popleft()
        flag = False
        for i in range(4):
            dx = x + dir[i][0]
            dy = y + dir[i][1]
            if 0 <= dx < w and 0 <= dy < h:
                if arr[dy][dx] == 'L' and not visited[dy][dx]:
                    flag = True
                    visited[dy][dx] = True
                    q.append((dx,dy,c+1))
        if not flag: countList.append(c)

    return max(countList)

h,w = map(int, input().split())
arr = [list(input()) for _ in range(h)]
lengthList = []
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'L':
            lengthList.append(BFS(j,i))
print(max(lengthList))