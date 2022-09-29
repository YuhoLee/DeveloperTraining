from collections import deque

# 초기 주사위 상태
dice = [[0,2,0],
        [4,1,3],
        [0,5,0],
        [0,6,0]]
# 방향
# 동, 남, 서, 북
dir = [[1,0],[0,1],[-1,0],[0,-1]]


# 방향에 따라 움직임
def move(d):
    tmp = dice[3][1]
    # 동쪽 이동
    if d == 0:
        dice[3][1] = dice[1].pop(-1)
        dice[1].insert(0,tmp)
    # 남쪽 이동
    elif d == 1:
        tmp = dice[3][1]
        for i in range(2,-1,-1):
            dice[i+1][1] = dice[i][1]
        dice[0][1] = tmp
    # 서쪽 이동
    elif d == 2:
        dice[3][1] = dice[1].pop(0)
        dice[1].append(tmp)
    # 북쪽 이동
    elif d == 3:
        tmp = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i+1][1]
        dice[3][1] = tmp


# 현재 지점에서 얻을 수 있는 점수를 계산
def get_score(x,y,target):
    visited = [[False]*m for _ in range(n)]
    q = deque()
    cnt = 1
    q.append((x,y))
    visited[y][x] = True
    while q:
        x,y = q.popleft()
        for dx,dy in dir:
            px,py = x+dx,y+dy
            if not(0 <= px < m and 0 <= py < n):
                continue
            # 방문하지 않았으며 현재 찾고있는 숫자와 같은 숫자일 시에만
            if not visited[py][px] and arr[py][px] == target:
                visited[py][px] = True
                cnt += 1
                q.append((px,py))

    return cnt*target


# init
n,m,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
d = 0
x,y = 0,0
res = 0
for _ in range(k):
    # 현재 가리키는 방향으로 이동
    dx,dy = dir[d]
    x,y = x+dx,y+dy
    # 그 지점이 범위를 벗어난 곳일 시
    if not(0 <= x < m and 0 <= y < n):
        # 현재 가리키는 방향의 반대방향을 가리키도록 함
        d = (d+2) % 4
        dx, dy = dir[d]
        # 순방향으로 한 번 와서 벗어났으니 반대방향으로 가야 하므로 2번 감
        x,y = x+2*dx, y+2*dy
    # 이동했을 때 바뀌는 주사위에 대해 작업 수행
    move(d)
    # 현재 지점에서 얻을 수 있는 점수 계산
    res += get_score(x,y,arr[y][x])
    # 주사위 바닥 숫자
    bottom = dice[3][1]
    # 현재 타일의 숫자
    curr = arr[y][x]
    # 주사위 바닥 숫자가 더 크면
    if bottom > curr:
        # 시계방향 회전
        d = (d+1) % 4
    elif bottom < curr:
        # 반시계방향 회전
        d = (d-1) % 4
print(res)