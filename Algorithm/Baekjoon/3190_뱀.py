dir = [[1,0],[0,1],[-1,0],[0,-1]]

# init
n = int(input())
k = int(input())
arr = [[0]*n for _ in range(n)]
arr_snake = [[9]*n for _ in range(n)]
arr_snake[0][0] = 0
for _ in range(k):
    y,x = map(int, input().split())
    arr[y-1][x-1] = 1
l = int(input())
rotate = [0]*l
for i in range(l):
    rotate[i] = list(input().split())

hx,hy = 0,0
tx,ty = 0,0
d = 0
time = 0
while True:
    dx,dy = dir[d]
    hx,hy = hx+dx,hy+dy
    if not(0 <= hx < n and 0 <= hy < n) or arr_snake[hy][hx] != 9:
        break
    # 다음 위치에 뱀 머리를 놓음
    arr_snake[hy][hx] = d
    # 해당 위치에 사과가 없다면
    if arr[hy][hx] != 1:
        # 꼬리의 방향을 가져옴
        ttx,tty = dir[arr_snake[ty][tx]]
        # 머리와 꼬리가 겹치지 않을 때는
        # 꼬리를 하나 줄여줌
        if not(hx==tx and hy==ty):
            arr_snake[ty][tx] = 9
        tx,ty = tx+ttx,ty+tty
    # 사과 없애기
    arr[hy][hx] = 0
    time += 1

    # 회전할게 있으며 현재 시간이 첫 인덱스 회전할 시간과 같을 시
    if len(rotate) > 0 and time == int(rotate[0][0]):
        # 반시계 방향
        if rotate[0][1] == 'L':
            d = (d-1) % 4
        # 시계 방향
        elif rotate[0][1] == 'D':
            d = (d+1) % 4
        # 방향 전환
        arr_snake[hy][hx] = d
        rotate.pop(0)
print(time+1)