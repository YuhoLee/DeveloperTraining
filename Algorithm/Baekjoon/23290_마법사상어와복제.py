from itertools import product

dir = [[0,0],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
shark_dir = [[0,0],[-1,0],[0,-1],[1,0],[0,1]]
shark_move = list(product(range(1,5),range(1,5),range(1,5)))[::-1]


def move_fish():
    buff = [[[]*1 for i in range(5)] for j in range(5)]
    for i in range(1,5):
        for j in range(1,5):
            if len(arr[i][j]) != 0:
                for d in arr[i][j]:
                    for ii in range(8):
                        px,py = i+dir[d][0],j+dir[d][1]
                        if 1 <= px < 5 and 1 <= py < 5 and not(px == shark[0] and py == shark[1]) and smell[px][py] == 0:
                            buff[px][py].append(d)
                            break
                        else:
                            d -= 1
                            if d <= 0: d = 8
                        if ii == 7:
                            buff[i][j].append(d)
    return buff


def hunt_shark():
    max_fish = 0
    res_x, res_y = shark[0], shark[1]
    res_visited = []
    for order in shark_move:
        px, py = shark[0], shark[1]
        cc = 0
        visited = []
        flag = False
        for ord in order:
            px,py = px+shark_dir[ord][0],py+shark_dir[ord][1]
            if not(1 <= px < 5 and 1 <= py < 5):
                flag = True
                break
            if (px,py) not in visited:
                cc += len(arr2[px][py])
                visited.append((px,py))
        if not flag:
            if max_fish <= cc:
                max_fish = cc
                res_x,res_y = px,py
                res_visited = visited[:]
    for vx,vy in res_visited:
        if len(arr2[vx][vy]) != 0:
            arr2[vx][vy] = []
            smell[vx][vy] = 3
    shark[0],shark[1] = res_x,res_y
    return max_fish


def smell_disappear():
    for i in range(1,5):
        for j in range(1,5):
            if smell[i][j] != 0: smell[i][j] -= 1


def copier():
    for x in range(1,5):
        for y in range(1,5):
            if len(arr2[x][y]) != 0:
                arr[x][y] += arr2[x][y]


m,s = map(int, input().split())
arr = [[[]*1 for i in range(5)] for j in range(5)]
fish = [0]*m
for i in range(m):
    fish[i] = tuple(map(int, input().split()))
    arr[fish[i][0]][fish[i][1]].append(fish[i][2])
shark = list(map(int, input().split()))
smell = [[0]*5 for _ in range(5)]

for i in range(s):
    arr2 = move_fish()
    cc = hunt_shark()
    smell_disappear()
    copier()
    m = m*2-cc
print(m)
