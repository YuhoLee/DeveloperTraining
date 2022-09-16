# r,u,l,d
dir1 = [(1,0),(0,-1),(-1,0),(0,1)]
# r,d,l,u
dir2 = [(1,0),(0,1),(-1,0),(0,-1)]

r,c,t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
machine = []
for i in range(r):
    if arr[i][0] == -1:
        machine.append((0,i))
        machine.append((0,i+1))
        break
mx1,my1 = machine[0]
mx2,my2 = machine[1]


for _ in range(t):
    buff = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                d = arr[i][j] // 5
                for dx,dy in [[1,0],[-1,0],[0,-1],[0,1]]:
                    px,py = j+dx,i+dy
                    if not(0 <= px < c and 0 <= py < r) or arr[py][px] == -1: continue
                    buff[py][px] += d
                    arr[i][j] -= d
    for i in range(r):
        for j in range(c):
            arr[i][j] += buff[i][j]

    px,py = mx1,my1
    dummy = 0
    for dx,dy in dir1:
        while True:
            px,py = px+dx,py+dy
            if not(0 <= px < c and 0 <= py <= my1):
                px,py = px-dx,py-dy
                break
            tmp = arr[py][px]
            arr[py][px] = dummy
            dummy = tmp
            if dummy == -1:
                arr[py][px] = -1
                break

    px, py = mx2, my2
    dummy = 0
    for dx, dy in dir2:
        while True:
            px, py = px + dx, py + dy
            if not (0 <= px < c and my2 <= py < r):
                px, py = px - dx, py - dy
                break
            tmp = arr[py][px]
            arr[py][px] = dummy
            dummy = tmp
            if dummy == -1:
                arr[py][px] = -1
                break

res = 0
for a in arr:
    res += sum(a)
print(res+2)
