import copy
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dir = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]


# 물고기 움직이기 및 상어가 먹을 수 있는 경우의 수에 대해 DFS
def dfs(sx, sy, score, arr):
    global max_score
    # 상어가 먹은 물고기에 대해 스코어를 더해주고 비교
    score += arr[sy][sx][0]
    max_score = max(max_score, score)
    # 먹었던 부위는 비워줌
    arr[sy][sx][0] = 0

    # 물고기 움직임
    for f in range(1, 17):
        fx, fy = -1, -1
        for y in range(4):
            for x in range(4):
                # 맵을 탐색하여 해당 물고기를 찾았다면
                if arr[y][x][0] == f:
                    # 물고기의 좌표를 가져옴
                    fx, fy = x, y
                    break
        # 못가져왔다면 없는 것이므로 다른 물고기 탐색
        if fx == -1 and fy == -1:
            continue
        # 물고기 방향 가져옴
        f_d = arr[fy][fx][1]

        # 8방향 전부 탐색 : 도중에 찾을 시 탈출
        for i in range(8):
            nd = (f_d+i) % 8
            dx, dy = dir[nd]
            px = fx + dx
            py = fy + dy
            # 범위내에 없고 상어의 좌표와 같다면 다음 방향 탐색
            if not (0 <= px < 4 and 0 <= py < 4) or (px == sx and py == sy):
                continue
            # 아니라면 방향 최신화
            arr[fy][fx][1] = nd
            # 물고기를 바꿔줌
            arr[fy][fx], arr[py][px] = arr[py][px], arr[fy][fx]
            break

    # 상어가 물고기 먹음 -> 방향이 기존 물고기 방향으로 바뀜
    s_d = arr[sy][sx][1]
    # 상어의 방향을 가져옴
    dx,dy = dir[s_d]
    for i in range(1, 5):
        px = sx + dx * i
        py = sy + dy * i
        # 물고기가 있을 때만 탐색
        if (0 <= px < 4 and 0 <= py < 4) and arr[py][px][0] > 0:
            # 3차원 배열을 슬라이싱으로 어떻게 복사할지 몰라서 deepcopy로 하였음
            dfs(px, py, score, copy.deepcopy(arr))


arr = [[] for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    buff = []
    for j in range(4):
        # 물고기 번호, 방향
        buff.append([data[2 * j], data[2 * j + 1] - 1])
    arr[i] = buff
max_score = 0
dfs(0, 0, 0, arr)
print(max_score)
