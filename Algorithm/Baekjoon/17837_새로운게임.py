dir = [[1,0],[-1,0],[0,-1],[0,1]]


# 게임을 진행하는 함수
def game():
    # 1번째 턴으로 시작
    cnt = 1
    while True:
        # 전체 말에 대해서
        for h in range(len(horse)):
            # 위치와 방향 가져옴
            y, x, d = horse[h]
            dx, dy = dir[d]

            # 방향에 해당하는 곳이 범위를 벗어났거나 파란색 블럭인 경우
            if not (0 <= y + dy < n and 0 <= x + dx < n) or arr[y + dy][x + dx] == 2:
                # 반대 방향으로 이동
                px, py = x - dx, y - dy
                # 방향 전환
                if horse[h][2] % 2 == 0:
                    dd = 1
                else:
                    dd = -1
                horse[h][2] += dd
                # 반대 방향으로 이동한 곳이 범위를 벗어나지 않고 흰 블럭이거나 빨간색 블럭일 경우
                if (0 <= py < n and 0 <= px < n) and arr[py][px] <= 1:
                    # 움직이는 말의 인덱스를 찾아서
                    idx = board[y][x].index(h)
                    # 움직여야 할 말들을 복사함
                    tmp = board[y][x][idx:]
                    # 말들의 위치를 옮겨줌
                    for s in tmp:
                        horse[s][0] = py
                        horse[s][1] = px
                    # 기존 위치는 말이 움직여서 일부 없어졌으므로 최신화
                    board[y][x] = board[y][x][:idx]
                    # 빨간색일 경우 움직여야 할 말들이 거꾸로 되야함.
                    if arr[py][px] == 1:
                        tmp = reversed(tmp)
                    # 목표 지점 위에 쌓음
                    board[py][px] += tmp

            else:
                # 흰색 / 적색
                if arr[y + dy][x + dx] <= 1:
                    # 움직이는 말의 인덱스를 찾아서
                    idx = board[y][x].index(h)
                    # 움직여야 할 말들을 복사함
                    tmp = board[y][x][idx:]
                    # 말들의 위치를 옮겨줌
                    for s in tmp:
                        horse[s][0] += dy
                        horse[s][1] += dx
                    # 기존 위치는 말이 움직여서 일부 없어졌으므로 최신화
                    board[y][x] = board[y][x][:idx]
                    # 빨간색일 경우 움직여야 할 말들이 거꾸로 되야함.
                    if arr[y + dy][x + dx] == 1:
                        tmp = reversed(tmp)
                    # 목표 지점 위에 쌓음
                    board[y + dy][x + dx] += tmp

            # 하나의 좌표에 4개 이상의 말이 있는 경우 return
            for i in range(n):
                for j in range(n):
                    if len(board[i][j]) >= 4:
                        return cnt

        # 1000턴을 넘어갔을 시 -1 반환
        if cnt > 1000: return -1
        cnt += 1


# init
n,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
board = [[[] for _ in range(n)] for _ in range(n)]
horse = [list(map(int, input().split())) for _ in range(k)]
for i,h in enumerate(horse):
    horse[i] = [h[0]-1,h[1]-1,h[2]-1]
for i,(y,x,d) in enumerate(horse):
    board[y][x].append(i)
print(game())

