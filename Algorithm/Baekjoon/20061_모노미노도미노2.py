# 한 칸짜리
def one(x,y,arr):
    px = x
    # 끝까지 도달할 때까지
    while px < 6:
        # 다음 탐색할 부분이 0이 아니라면
        if arr[px][y] != 0:
            # 현재 위치에 놓기
            arr[px-1][y] = 1
            return
        px += 1
    # 끝까지 도달하고 탈출 -> 제일 끝에 놓기
    arr[px-1][y] = 1


# 가로로 길쭉한 2칸짜리
def row(x,y,arr):
    px = x
    # 끝까지 도달할 때까지
    while px < 6:
        # 두 타일의 다음 탐색할 부분이 하나라도 0이 아니라면
        if arr[px][y] != 0 or arr[px][y+1] != 0:
            # 현재 위치에 놓기
            arr[px-1][y] = 1
            arr[px-1][y+1] = 1
            return
        px += 1
    # 끝까지 도달하고 탈출 -> 제일 끝에 놓기
    arr[px-1][y], arr[px-1][y+1] = 1,1


# 세로로 길쭉한 2칸짜리
def col(x,y,arr):
    px =  x
    while px < 5:
        # 아래칸의 다음 탐색할 부분이 0이 아니라면
        if arr[px+1][y] != 0:
            arr[px-1][y] = 1
            arr[px][y] = 1
            return
        px += 1
    # 끝까지 도달하고 탈출 -> 제일 끝에 놓기
    arr[px-1][y], arr[px][y] = 1,1


def play():
    global score
    for t,x,y in block:
        # 타일 놓기
        if t == 1:          # 1칸짜리
            one(0,y,green)
            one(0,x,blue)
        elif t == 2:        # 가로 2칸짜리
            row(0,y,green)  # green 기준에서는 가로
            col(0,x,blue)   # blue 기준에서는 세로
        elif t == 3:        # 세로 2칸짜리
            col(0,y,green)  # green 기준에서는 세로
            row(0,x,blue)   # blue 기준에서는 가로로

       # 가득 찬 줄 체크
        for i in range(2,6):
            if sum(green[i]) == 4:      # 행의 합이 4 -> 행이 가득참
                green.pop(i)            # 해당 행을 빼주고
                green.insert(0,[0]*4)   # 새로운 빈 행을 제일 위에 추가
                score += 1
            if sum(blue[i]) == 4:       # 행의 합이 4 -> 행이 가득참
                blue.pop(i)             # 해당 행을 빼주고
                blue.insert(0,[0]*4)    # 새로운 빈 행을 제일 위에 추가
                score += 1

        # 옅은 칸 부분 체크
        for i in range(2):              # 행 1에 대해서 체크
            if sum(green[1]) > 0:       # 행 1이 한 칸이라도 차있다면
                green.pop(-1)           # 마지막 행을 빼주고
                green.insert(0,[0]*4)   # 새로운 빈 행을 제일 위에 추가
            if sum(blue[1]) > 0:        # 행 1이 한 칸이라도 차있다면
                blue.pop(-1)            # 마지막 행을 빼주고
                blue.insert(0,[0]*4)    # 새로운 빈 행을 제일 위에 추가


# init
n = int(input())
block = [tuple(map(int, input().split())) for _ in range(n)]
green = [[0]*4 for _ in range(6)]
blue = [[0]*4 for _ in range(6)]
score = 0
tile = 0
play()
# 전체 타일 수 카운트
tile += sum([sum(g) for g in green])
tile += sum([sum(b) for b in blue])
print(score)
print(tile)