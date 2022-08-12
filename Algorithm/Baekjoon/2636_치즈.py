import sys
sys.setrecursionlimit(10**6)

def DFS(arr,y,x):
    global h,w,c
    visited[y][x] = True
    for i in range(4):
        dy = y + dir[i][0]
        dx = x + dir[i][1]
        if 0 <= dy < h and 0 <= dx < w:
            if arr[dy][dx] == 0 and not visited[dy][dx] :
                DFS(arr,dy,dx)
            elif arr[dy][dx] == 1 and not visited[dy][dx]:
                arr[dy][dx] = 0
                visited[dy][dx] = True
                c += 1

h,w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
dir = [[1,0],[-1,0],[0,1],[0,-1]]
c = -1
count = 0
cheese = []
while c != 0:
    c = 0
    visited = [[False] * w for _ in range(h)]
    if not visited[0][0] and arr[0][0] == 0:
        DFS(arr,0,0)
    if c == 0: break
    else:
        cheese.append(c)
        count += 1

print(count)
print(cheese[-1])