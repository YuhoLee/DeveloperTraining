from collections import deque

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs():
    global tomato
    cnt = 0
    buff = []
    q = deque()
    for t in tomato:
        q.append(t)
        visited[t[1]][t[0]] = True
    while q:
        x, y= q.popleft()
        for dx, dy in dir:
            px, py = x + dx, y + dy
            if not (0 <= px < m and 0 <= py < n): continue
            if not visited[py][px] and box[py][px] == 0:
                box[py][px] = 1
                cnt += 1
                visited[py][px] = True
                buff.append([px, py])
    tomato = buff[:]
    return cnt


def is_full_well():
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return False
    return True


m, n= map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
tomato = []
bad_tomato = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 1: tomato.append([j, i])
        elif box[i][j] == 0: bad_tomato += 1
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
