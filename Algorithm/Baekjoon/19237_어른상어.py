dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]


# 상어의 움직임에 대한 결과 함수
def move_shark():
    # 전체 상어 좌표에 대해
    for i in range(1, len(sharkList)):
        # 상어가 살아있으면
        if sharkList[i] is not None:
            # 좌표 및 방향 가져오기
            x, y, d = sharkList[i]
            # 빈 칸에 들어갈 수 있는지에 대한 flag
            success = False
            # 현재 가지고 있는 방향에 대한 다음 방향의 우선순위를 가져옴
            for dd in shark_priority[i-1][d]:
                dx,dy = dir[dd]
                px, py = x + dx, y + dy
                # 범위를 넘지 않고
                if 0 <= px < n and 0 <= py < n:
                    # 냄새가 없다면
                    if smell[py][px] is None:
                        # 빈 칸에 들어갈 수 있음!
                        success = True
                        # 만약 해당 칸에 다른 상어가 위치해 있다면
                        # 작은 순서대로 순차적으로 움직이기에 다른 상어가 있다면 무조건 자신보다 작은 상어
                        # 따라서 죽음...
                        if 0 < arr[py][px] < i:
                            arr[y][x] = 0
                            sharkList[i] = None
                        # 다른 상어가 없다면
                        # 해당 위치로 이동 및 방향 조정
                        else:
                            arr[y][x] = 0
                            arr[py][px] = i
                            sharkList[i] = [px,py,dd]
                        break

            # 빈 칸에 들어가지 못했을 시
            if not success:
                # 현재 가지고 있는 방향에 대한 다음 방향의 우선순위를 가져옴
                for dd in shark_priority[i-1][d]:
                    dx, dy = dir[dd]
                    px, py = x + dx, y + dy
                    if 0 <= px < n and 0 <= py < n:
                        # 냄새가 존재하고 해당 냄새의 자취가 자신의 자취라면
                        # 해당 위치로 이동 및 방향 조절
                        if smell[py][px] is not None and smell[py][px][1] == i:
                            arr[y][x] = 0
                            arr[py][px] = i
                            sharkList[i] = [px, py, dd]
                            break


# 냄새를 사라지게 하는 함수
def smell_disappear():
    # 전체 냄새 칸에 대해
    for i in range(n):
        for j in range(n):
            # 냄새가 존재한다면
            if smell[i][j] is not None:
                # 1감소
                smell[i][j][0] -= 1
                # 0이 되었을 시 냄새를 없앰
                if smell[i][j][0] == 0:
                    smell[i][j] = None


# 상어가 냄새를 풍기도록 함
def smelling():
    # 전체 상어에 대해
    for i in range(1,len(sharkList)):
        # 상어가 살아있다면
        if sharkList[i] is not None:
            # 좌표를 가져와서 k만큼 지속되는 냄새를 생성
            x,y,_ = sharkList[i]
            smell[y][x] = [k,i]


# 살아있는 상어 수를 세는 함수
def count_shark():
    cnt = 0
    for i in range(1,len(sharkList)):
        if sharkList[i] is not None:
            cnt += 1
    return cnt


# init
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
curr_shark_dir = list(map(int, input().split()))
sharkList = [None] * (m + 1)
smell = [[None] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            sharkList[arr[i][j]] = [j, i, curr_shark_dir[arr[i][j]-1] - 1]
            smell[i][j] = [k, arr[i][j]]
shark_priority = []
for _ in range(m):
    shark_priority.append([[i - 1 for i in list(map(int, input().split()))] for _ in range(4)])


time = 0
while True:
    time += 1
    # time > 1000 -> time over
    if time > 1000:
        print(-1)
        break
    # 상어 움직임
    move_shark()
    # 냄새 사라짐
    smell_disappear()
    # 냄새 풍기기
    smelling()
    # 상어 수 세기
    # 상어가 1마리만 남았을 시 출력
    if count_shark() == 1:
        print(time)
        break