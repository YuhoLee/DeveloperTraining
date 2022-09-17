from collections import deque


# BFS 탐색
# 인자로 받은 좌표에서 시작하여 그룹이 될 수 있는 블럭 탐색
def BFS(p):
    q = deque()
    count = 1               # 그룹이 될 수 있는 블럭 개수
    rbw = 0                 # 무지개 블럭 개수
    point = []              # 그룹을 이루는 좌표 리스트
    mn = arr[p[1]][p[0]]    # 메인이 되는 블럭(제일 처음 탐색한 블럭 종류)
    visited[p[1]][p[0]] = True
    q.append((p[0],p[1]))
    while q:
        x,y = q.popleft()
        # 큐에 들어간 좌표들은 그룹이므로 point에 추가
        point.append((x,y))
        for dx,dy in [(1,0),(-1,0),(0,-1),(0,1)]:
            px,py = x+dx,y+dy
            if not(0 <= px < n and 0 <= py < n):
                continue
            # 방문하지 않았으며 메인이 되는 블럭과 같거나 무지개블럭일 시 그룹에 추가
            if not visited[py][px]:
                if arr[py][px] == mn or arr[py][px] == 0:
                    if arr[py][px] == 0:
                        rbw += 1
                    count += 1
                    visited[py][px] = True
                    q.append((px,py))
    return point, count, rbw


# 중력 작용 함수
def gravity():
    # 제일 아래는 신경쓰지 않아도 되므로 아래에서 2번째부터 시작
    for i in range(n-2,-1,-1):
        for j in range(n):
            # 검은색을 제외한 블럭일 시
            if arr[i][j] >= 0:
                gx,gy = j,i
                while True:
                    # 맵을 나가지 않는 범위 내에서 다음 칸이 빈칸이면
                    if gy+1 < n and arr[gy+1][gx] == -2:
                        gy += 1
                    else:
                        tmp = arr[i][j]
                        arr[i][j] = -2
                        arr[gy][gx] = tmp
                        break


# 90도 반시계 회전 함수
# 2차원 배열의 각 행에 대해 reverse한 후 전치행렬을 적용하면 90도 반시계 회전
def rotate():
    buff = [a[:] for a in arr[:]]
    for i,b in enumerate(buff):
        buff[i] = b[::-1]
    return list(map(list,zip(*buff)))


n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
score = 0

while True:
    visited = [[False]*n for _ in range(n)]
    res_pointList = [(n,n)]
    res_cnt = 0
    res_rbwCount = 0
    # 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
    # 라는 조건은 이중 for문을 통해 위에서 아래로, 왼쪽에서 오른쪽으로 배열을 탐색하며 해당 지점이 일반블럭일 때 그 지점을 기준 블럭으로 잡으라는 말로 해석 가능
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 and not visited[i][j]:
                flag = False
                pointList, cnt, rbwCount = BFS((j,i))
                # 우선순위를 적용하여 최선의 그룹 찾기
                # 그룹블럭 수 > 무지개블럭 수 > 기준블럭 행 > 기준블럭 열
                if res_cnt < cnt: flag = True
                elif res_cnt == cnt:
                    if res_rbwCount < rbwCount: flag = True
                    elif res_rbwCount == rbwCount:
                        if res_pointList[0][1] < pointList[0][1]: flag = True
                        elif res_pointList[0][1] == pointList[0][1]:
                            if res_pointList[0][0] < pointList[0][0]: flag = True
                # 최선의 그룹을 찾았을 시
                # 결과 값들을 최신화
                if flag:
                    res_pointList = pointList
                    res_cnt = cnt
                    res_rbwCount = rbwCount
                # 무지개블럭은 그룹 탐색 시 모두 활용할 수 있어야 하므로
                # visited를 다시 False로 바꿔줌
                for x,y in pointList:
                    if arr[y][x] == 0:
                        visited[y][x] = False

    # 최선의 그룹 블럭 수가 2개 이상이 아닐 시 (그룹이 아님)
    if res_cnt <= 1:
        break
    score += (res_cnt**2)
    # 블럭 제거
    for x,y in res_pointList:
        arr[y][x] = -2
    # 중력 -> 90도 반시계 회전 -> 중력
    gravity()
    arr = rotate()
    gravity()

print(score)