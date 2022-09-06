# 움직이는 방향별 현재 좌표 기준 흩어지는 위치 및 비율
left = [(0,-2,0.02),(-1,-1,0.1),(0,-1,0.07),(1,-1,0.01),(-2,0,0.05),(-1,1,0.1),(0,1,0.07),(1,1,0.01),(0,2,0.02)]
down = [(-1,-1,0.01),(1,-1,0.01),(-2,0,0.02),(-1,0,0.07),(1,0,0.07),(2,0,0.02),(-1,1,0.1),(1,1,0.1),(0,2,0.05)]
right = [(0,-2,0.02),(-1,-1,0.01),(0,-1,0.07),(1,-1,0.1),(2,0,0.05),(-1,1,0.01),(0,1,0.07),(1,1,0.1),(0,2,0.02)]
up = [(0,-2,0.05),(-1,-1,0.1),(1,-1,0.1),(-2,0,0.02),(-1,0,0.07),(1,0,0.07),(2,0,0.02),(-1,1,0.01),(1,1,0.01)]
move_ratio = [left, down, right, up]

# 방향
dir = [(-1,0),(0,1),(1,0),(0,-1)]


# 다음 방향을 반환하는 함수
def next_dir(i):
    i += 1
    if i == 4:
        i = 0
    return i


# init
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
storm_x,storm_y = n//2,n//2
visited[storm_y][storm_x] = True
direction = 0
out_sand = 0

while True:
    storm_x += dir[direction][0]
    storm_y += dir[direction][1]
    visited[storm_y][storm_x] = True
    remained_sand = arr[storm_y][storm_x]
    for dd in move_ratio[direction]:
        dx,dy,ratio = dd[0],dd[1],dd[2]
        px,py = storm_x+dx, storm_y+dy
        spread_sand = int(arr[storm_y][storm_x] * ratio)
        remained_sand -= spread_sand
        if not(0 <= px < n and 0 <= py < n):
            out_sand += spread_sand
        else:
            arr[py][px] += spread_sand
    ax,ay = storm_x+dir[direction][0], storm_y+dir[direction][1]
    if not(0 <= ax < n and 0 <= ay < n):
        out_sand += remained_sand
    else: arr[ay][ax] += remained_sand
    arr[storm_y][storm_x] = 0

    nx,ny = storm_x + dir[next_dir(direction)][0], storm_y + dir[next_dir(direction)][1]
    if not visited[ny][nx]:
        direction = next_dir(direction)
    if storm_x == 0 and storm_y == 0: break

print(out_sand)
