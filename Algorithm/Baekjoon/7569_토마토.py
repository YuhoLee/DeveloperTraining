from collections import deque

dir = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]


def bfs():
    global tomato
    cnt = 0
    buff = []
    q = deque()
    for t in tomato:
        q.append(t)
        visited[t[2]][t[1]][t[0]] = True
    while q:
        x, y, z = q.popleft()
        for dx, dy, dz in dir:
            px, py, pz = x + dx, y + dy, z + dz
            if not (0 <= px < m and 0 <= py < n and 0 <= pz < h): continue
            if not visited[pz][py][px] and box[pz][py][px] == 0:
                box[pz][py][px] = 1
                cnt += 1
                visited[pz][py][px] = True
                buff.append([px, py, pz])
    tomato = buff[:]
    return cnt


def is_full_well():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    return False
    return True


m, n, h = map(int, input().split())
box = []
for _ in range(h):
    box.append([list(map(int, input().split())) for _ in range(n)])
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
tomato = []
bad_tomato = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1: tomato.append([k, j, i])
            elif box[i][j][k] == 0: bad_tomato += 1
if bad_tomato == 0:
    print(0)
else:
    time = 0
    flag = False
    while True:
        time += 1
        res = bfs()
        if res == 0:
            break
        if is_full_well():
            flag = True
            break
    if flag: print(time)
    else: print(-1)
