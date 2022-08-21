cctv=[[],
      [[(1,0)],[(-1,0)],[(0,1)],[(0,-1)]],  # cctv1
      [[(1,0),(-1,0)],[(0,1),(0,-1)]],      # cctv2
      [[(-1,0),(0,1)],[(0,-1),(1,0)],[(-1,0),(0,-1)],[(1,0),(0,1)]],    # cctv3
      [[(-1,0),(0,1),(0,-1)],[(1,0),(0,1),(0,-1)],[(1,0),(-1,0),(0,-1)],[(1,0),(-1,0),(0,1)]],  # cctv4
      [[(1,0),(-1,0),(0,1),(0,-1)]]]    # cctv5


def DFS(idx, arr, blank):
    global res, idx_max
    if idx == idx_max:
        if res > blank:
            res = blank
        return

    type = location[idx][0]
    x,y = location[idx][1], location[idx][2]
    for case in cctv[type]:
        buff = [ar[:] for ar in arr]
        total = blank
        for dx,dy in case:
            cx,cy = x,y
            while True:
                cx,cy = cx+dx,cy+dy
                if not(0 <= cx < w and 0 <= cy < h): break
                if buff[cy][cx] == 0:
                    buff[cy][cx] = '#'
                    total -= 1
                elif arr[cy][cx] == 6: break
        DFS(idx+1,buff,total)


h,w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
location = []
idx_max = 0
total = h*w
for i in range(h):
    for j in range(w):
        if arr[i][j] != 0:
            total -= 1
            if arr[i][j] != 6:
                location.append((arr[i][j],j,i))
                idx_max += 1
res = float('inf')
buff = [ar[:] for ar in arr]
DFS(0,buff,total)
print(res)