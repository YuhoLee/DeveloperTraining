t = int(input())
for test in range(1,t+1):
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    home_point = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1: home_point.append((j,i))

    res = 0
    for y in range(n):
        for x in range(n):
            max_hc = 0
            hc = 0
            if arr[y][x] == 1:
                hc,max_hc = 1,1
            for d in range(1,n*2-1):
                buff_hc = hc
                for dx in range(0,d+1):
                    dy = d-dx
                    if dx == 0 or dy == 0:
                        if dx == 0:
                            dir = [[0,-1],[0,1]]
                        elif dy == 0:
                            dir = [[-1,0],[1,0]]
                    else: dir = [[1,1],[-1,-1],[1,-1],[-1,1]]
                    for dir_x, dir_y in dir:
                        px = x+dx*dir_x
                        py = y+dy*dir_y
                        if not(0 <= px < n and 0 <= py < n): continue
                        if arr[py][px] == 1:
                            buff_hc += 1
                k = d+1
                score = buff_hc*m-(k**2+(k-1)**2)
                if score >= 0:
                    if max_hc < buff_hc:
                        max_hc = buff_hc
                hc = buff_hc
            if res < max_hc:
                res = max_hc

    print("#{} {}".format(test,res))
