from collections import deque


def calc_sum():
    return sum([sum(p) for p in plate])


def search(x,y):
    global cnt
    q = deque()
    q.append((x,y))
    visited[y][x] = True
    target = plate[y][x]
    c = 1
    while q:
        qx,qy = q.popleft()
        plate[qy][qx] = 0
        cnt -= 1
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            px,py = qx+dx,qy+dy
            if not(0 <= py < n): continue
            if px == m: px = 0
            if not visited[py][px] and plate[py][px] == target:
                c += 1
                q.append((px,py))
                visited[py][px] = True
    if c > 1: return True
    else: return False


n,m,t = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(n)]
action = [list(map(int, input().split())) for _ in range(t)]
cnt = n*m

for x,d,k in action:
    visited = [[False]*m for _ in range(n)]
    for i in range(x,n+1):
        if i % x == 0:
            for _ in range(k):
                if d == 0:
                    tmp = plate[i-1].pop(-1)
                    plate[i-1].insert(0,tmp)
                elif d == 1:
                    tmp = plate[i-1].pop(0)
                    plate[i-1].append(tmp)
    flag = False
    for i in range(n):
        for j in range(m):
            if plate[i][j] != 0 and not visited[i][j]:
                buff = plate[i][j]
                if not search(j,i):
                    visited[i][j] = False
                    plate[i][j] = buff
                    cnt += 1
                else: flag = True

    if calc_sum() == 0: break

    if not flag:
        avg = calc_sum() / cnt
        for i in range(n):
            for j in range(m):
                if 0 < plate[i][j] < avg: plate[i][j] += 1
                elif plate[i][j] > avg: plate[i][j] -= 1

print(calc_sum())
