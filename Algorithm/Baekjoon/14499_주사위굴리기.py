# 초기 주사위 상태
dice = [[0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]]

dir = [[1,0],[-1,0],[0,-1],[0,1]]

# 방향 별 움직임에 따른 주사위 전개도 변화
def move(d):
    tmp = dice[3][1]
    # 동쪽 이동
    if d == 0:
        dice[3][1] = dice[1].pop(-1)
        dice[1].insert(0,tmp)
    # 남쪽 이동
    elif d == 3:
        tmp = dice[3][1]
        for i in range(2,-1,-1):
            dice[i+1][1] = dice[i][1]
        dice[0][1] = tmp
    # 서쪽 이동
    elif d == 1:
        dice[3][1] = dice[1].pop(0)
        dice[1].append(tmp)
    # 북쪽 이동
    elif d == 2:
        tmp = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i+1][1]
        dice[3][1] = tmp


n,m,y,x,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dirList = list(map(int, input().split()))
px,py = x,y
for d in dirList:
    dx,dy = dir[d-1]
    # 일단 다음 칸으로 이동한 후에
    x,y = x+dx,y+dy
    # 범위를 벗어났을 시 원래대로 돌려줌
    if not (0 <= x < m and 0 <= y < n):
        x,y = x-dx,y-dy
        continue
    move(d-1)
    # 현재 위치 타일이 0이라면
    if arr[y][x] == 0:
        # 해당 타일에 주사위 밑면의 숫자를 넣음
        arr[y][x] = dice[3][1]
    # 타일이 0이 아니라면 
    else:
        # 다이스의 밑면을 타일의 숫자로 만들고 타일을 0으로 만듦
        dice[3][1] = arr[y][x]
        arr[y][x] = 0
    # 다이스 윗면 출력
    print(dice[1][1])
