from collections import deque

# (북,동,남,서) 의 왼쪽
dir = [[-1,0],[0,-1],[1,0],[0,1]]
# (북,동,남,서) 의 뒤쪽
back = [[0,1],[-1,0],[0,-1],[1,0]]
# 왼쪽으로 회전했을 때 바라보는 방향
face = [3,0,1,2]


def clean(ix,iy,start):
    count = 0
    q = deque()
    q.append((ix,iy,start))
    while q:
        x,y,f = q.popleft()
        if arr[y][x] == 0:
            arr[y][x] = 2
            count += 1
        flag = False
        for i in range(4):
            dx,dy = dir[f]
            px,py = x+dx,y+dy
            if not(0<=px<w and 0<=py<h) or arr[py][px] == 1:
                f = face[f]
                continue
            if arr[py][px] == 0:
                q.append((px,py,face[f]))
                flag = True
                break
            else:
                f = face[f]
        if not flag:
            px, py = x + back[f][0], y + back[f][1]
            if arr[py][px] != 1:
                x,y = x+back[f][0],y+back[f][1]
                q.append((x,y,f))
            else: break
    return count


h, w = map(int, input().split())
y,x,f = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
print(clean(x,y,f))