from itertools import combinations
from collections import deque

h,w = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]


def BFS():
    q = deque()
    # 맵 복사
    buff = []
    for a in arr:
        buff.append(a[:])
    # 방문 여부
    visited = [[False]*w for _ in range(h)]
    # 빈 영역 개수 세기 및 바이러스 좌표 큐에 넣기
    cnt = 0
    for i in range(h):
        for j in range(w):
            if buff[i][j] == 0: cnt += 1
            if buff[i][j] == 2:
                q.append((j,i))
                visited[i][j] = True
    while q:
        # 큐에서 좌표를 꺼냄
        x,y = q.popleft()
        # 사방 탐색
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            px,py = x+dx,y+dy
            # 범위를 벗어나지 않았을 때
            if 0 <= px < w and 0 <= py < h:
                # 빈 칸이며 방문하지 않았을 시
                if buff[py][px] == 0 and not visited[py][px]:
                    # 바이러스 확산
                    q.append((px,py))
                    visited[py][px] = True
                    buff[py][px] = 2
                    cnt -= 1
    return cnt


# 세울 수 있는 전체 경우의 수 생성
l = []
for i in range(h):
    for j in range(w):
      l.append((j,i))
com = combinations(l,3)

res = 0
# 경우의 수 하나씩 꺼내서 살펴보기
for c in com:
    x1,y1 = c[0]
    x2,y2 = c[1]
    x3,y3 = c[2]
    # 세 위치가 모두 빈공간일 경우
    if arr[y1][x1] == 0 and arr[y2][x2] == 0 and arr[y3][x3] == 0:
        # 벽 세우기
        arr[y1][x1], arr[y2][x2], arr[y3][x3] = 1,1,1
        # BFS를 통해 안전영역의 최댓값 구하기
        res = max(res,BFS())
        # 다음 경우의 수를 위해 벽 허물기
        arr[y1][x1], arr[y2][x2], arr[y3][x3] = 0,0,0
print(res)