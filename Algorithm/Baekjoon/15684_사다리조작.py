# i번의 세로선 결과가 i인지 검사
def simulation():
    # 첫 flag True
    flag = True
    # 전체의 세로선에 대해
    for i in range(n):
        x,y = i,0
        # 결과에 도달할 때까지
        while y < h:
            # 해당 지점에 좌/우로 뻗는 선이 존재 할 때
            if ladder[y][x]:
                # 좌로 뻗는 선이 존재한다면
                if 0 <= x-1 < n and ladder[y][x-1] == ladder[y][x]:
                    x -= 1  # 이동
                # 우로 뻗는 선이 존재한다면
                elif 0 <= x+1 < n and ladder[y][x+1] == ladder[y][x]:
                    x += 1  # 이동
            # 아래로 한 칸 이동
            y += 1
        # 하나라도 매칭 안되면 flag False 후 반복문 탈출
        if i != x:
            flag = False
            break
    # 검사 결과 반환
    return flag


# 새로 긋는 선을 기준으로 백트래킹
def DFS(x,y,c):
    global c_min
    # 그어진 선이 3개보다 많을 시 해당 경우의 수 종료
    if c > 3: return
    # DFS에서 끝난 지점을 가져옴 -> 탐색한 지점을 다시 탐색하지 않기 위함
    i = y
    j = x
    # 가로선 끝까지
    while i < h:
        # 세로선 끝 - 1 : 선을 왼쪽에서 오른쪽으로 긋기에
        while j < n-1:
            # 해당 지점에 이어진 선이 존재하지 않고, 해당 지점의 오른쪽 지점 또한 선이 존재하지 않다면
            if not ladder[i][j] and not ladder[i][j+1]:
                # 선을 그어줌
                ladder[i][j], ladder[i][j+1] = c+1,c+1
                # 검사
                if simulation():
                    # 만족 시 선 개수 최소값 최신화
                    if c < c_min: c_min = c
                else:
                    # 아닐 시 해당 경우에서 선을 하나 더 긋도록 함
                    DFS(j, i, c + 1)
                # 그었던 선을 없앰
                ladder[i][j], ladder[i][j+1] = 0,0
            j += 1
        j = 0
        i += 1


# init
n,m,h = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(m)]
ladder = [[0]*n for _ in range(h)]
c_min = float('inf')
for i,(a,b) in enumerate(info):
    ladder[a-1][b-1] = -i-1
    ladder[a-1][b] = -i-1

# 선을 긋지 않은 경우에도 검사 결과가 True일 수 있으므로 처음부터 검사
if simulation(): print(0)
else:
    DFS(0,0,1)
    if c_min != float('inf'): print(c_min)
    else: print(-1)
