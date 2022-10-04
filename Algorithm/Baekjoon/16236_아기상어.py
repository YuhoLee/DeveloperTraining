from collections import deque

# BFS 사냥
def hunt():
    global x,y, shark, exp, res
    # 방문 여부 확인
    visited = [[False] * n for _ in range(n)]
    # 먹을 물고기가 있는지 없는지에 대한 flag 변수
    flag = False
    q = deque()
    q.append((x,y,0))
    visited[y][x] = True
    # 잡아먹을 수 있는 물고기 중 거리가 같은 물고기들에 대한 리스트
    can = []
    while q:
        cx,cy,cc = q.popleft()
        # 잡아 먹을 물고기가 있을 때 해당 물고기보다 거리가 더 먼 경우 -> 탈출
        # BFS는 최단거리에 많이 사용
        if len(can) != 0 and can[0][2] < cc: break
        # 물고기인데 아기상어보다 작은 경우
        if 0 < arr[cy][cx] < shark:
            # 먹을 물고기 있음!
            flag = True
            can.append((cx,cy,cc))
        # 사방탐색
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            px,py = cx+dx,cy+dy
            # 범위 여부 확인
            if not(0 <= px < n and 0 <= py < n): continue
            # 방문하지 않았으며 빈칸이거나 아기상어보다 작거나 같은 물고기가 있는 칸일 시 이동
            if not visited[py][px] and (arr[py][px] == 0 or arr[py][px] <= shark):
                visited[py][px] = True
                q.append((px,py,cc+1))
    # 먹을 수 있는 물고기가 있다면
    if flag:
        # 행이 작은 순 > 열이 작은 순 으로 정렬
        # 거리는 다 같아서 따로 정렬 안했음
        can.sort(key=lambda x: (x[1],x[0]))
        rx,ry,time = can[0]
        # 소요 시간 더해주기
        res += time
        # 기존 위치를 0으로 하고 잡아먹은 위치를 상어 위치로 함
        arr[y][x] = 0
        arr[ry][rx] = 9
        x,y = rx,ry

        exp += 1
        # 해당 조건식을 안해주면 아기상어가 자기를 잡아먹음... -> 무한루프
        if shark < 7:
            # 같아지면 상어 크기 증가하고 먹은 물고기 0으로 초기화
            if exp == shark:
                shark += 1
                exp = 0
    return flag


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
x,y = -1,-1
shark = 2
exp = 0
res = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            x,y = j,i

# hunt가 False일 때까지 반복
# -> 사냥할 물고기가 없어질 때까지 반복
while hunt():
    pass
print(res)
