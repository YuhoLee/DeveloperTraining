# r,u,l,d
dir1 = [(1,0),(0,-1),(-1,0),(0,1)]
# r,d,l,u
dir2 = [(1,0),(0,1),(-1,0),(0,-1)]

r,c,t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
machine = []
for i in range(r):
    if arr[i][0] == -1:
        machine.append((0,i))
        machine.append((0,i+1))
        break

# 공기청정기의 좌표
mx1,my1 = machine[0]
mx2,my2 = machine[1]

# t만큼 반복시행
for _ in range(t):
    # 각 지점으로 흩어질 먼지들의 양을 저장하는 리스트
    buff = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            # 해당 지점이 로봇이 아니고 미세먼지가 있을 시
            if arr[i][j] > 0:
                # 흩어지는 양
                d = arr[i][j] // 5
                for dx,dy in [[1,0],[-1,0],[0,-1],[0,1]]:
                    px,py = j+dx,i+dy
                    # 인접 칸이 맵 범위를 벗어나고 로봇일 시 시행X
                    if not(0 <= px < c and 0 <= py < r) or arr[py][px] == -1: continue
                    # 더해지는 buff에는 흩어지는 양을 더해주고
                    buff[py][px] += d
                    # 기존 리스트에서는 그 만큼 빼줌
                    arr[i][j] -= d
    # arr에 buff를 더해주어 흩어진 후의 결과 도출
    for i in range(r):
        for j in range(c):
            arr[i][j] += buff[i][j]

    # 공기청정기 순환
    # 윗쪽 순환(반시계방향)
    px,py = mx1,my1
    dummy = 0
    for dx,dy in dir1:
        while True:
            px,py = px+dx,py+dy
            # 윗쪽 순환 범위 내에서만 동작
            if not(0 <= px < c and 0 <= py <= my1):
                px,py = px-dx,py-dy
                break
            # 현재 지점의 미세먼지 양을 저장해놓고
            # 이전에 밀려온 미세먼지의 양을 넣은 후
            # 저장해놓은 미세먼지는 다음 칸에 밀려야하기 때문에 dummy에 저장
            tmp = arr[py][px]
            arr[py][px] = dummy
            dummy = tmp
            # dummy가 -1
            # -> 공기청정기이므로 다시 -1로 바꿔줌
            if dummy == -1:
                arr[py][px] = -1
                break

    # 아랫쪽 순환(시계방향)
    px, py = mx2, my2
    dummy = 0
    for dx, dy in dir2:
        while True:
            px, py = px + dx, py + dy
            # 아랫쪽 순환 범위 내에서만 동작
            if not (0 <= px < c and my2 <= py < r):
                px, py = px - dx, py - dy
                break
            # 현재 지점의 미세먼지 양을 저장해놓고
            # 이전에 밀려온 미세먼지의 양을 넣은 후
            # 저장해놓은 미세먼지는 다음 칸에 밀려야하기 때문에 dummy에 저장
            tmp = arr[py][px]
            arr[py][px] = dummy
            dummy = tmp
            # dummy가 -1
            # -> 공기청정기이므로 다시 -1로 바꿔줌
            if dummy == -1:
                arr[py][px] = -1
                break

res = 0
# 남은 미세먼지 전체를 더해줌
for a in arr:
    res += sum(a)
# 공기청정기가 -1로 2칸 존재하여 위에서 계산 시 더해졌기에
# 결과값에 2를 더해줌
print(res+2)
