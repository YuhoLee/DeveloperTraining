dir = [[1,0],[0,1],[-1,0],[0,-1]]

# k의 max 사이즈
mSize = 300 // 2
t = int(input())
for test in range(1,t+1):
    # init
    n,m,k = map(int, input().split())
    # 배양 용기의 크기가 정해져 있지 않아
    # k의 최대 사이즈 300을 감안하여
    # 세로 (300*2 + n), 가로 (300*2 + m) 으로 설정
    arr = [[0] * (2 * mSize + m) for _ in range(mSize)]
    arr += [[0] * mSize + list(map(int, input().split())) + [0] * mSize for _ in range(n)]
    arr += [[0] * (2 * mSize + m) for _ in range(mSize)]

    # 세포가 저장될 dict
    cell = {}

    # 첫 시작은 SIZE,SIZE
    # 크기는 세로 n, 가로 m만큼
    # 입력 받은 리스트에 대해 0이 아닌 것들을 전부 cell dict에 가져옴
    for i in range(mSize, n + mSize):
        for j in range(mSize, m + mSize):
            if arr[i][j] != 0:
                cell[(j,i)] = [-1,0,arr[i][j]]

    # k번 반복
    for _ in range(k):
        # dict의 모든 키(좌표)를 가져옴
        keys = list(cell.keys())

        for (x,y) in keys:
            # 좌표에 대한 활성/비활성 상태, 현재 세포 진행, 살아있을 수 있는 시간을 가져옴
            state, curr, live = cell[(x,y)]

            # 현재 세포 진행 +1씩
            cell[(x,y)][1] += 1
            # 활성 체크
            # 세포가 비활성화 상태이며 활성 상태에 도달할 수 있을 때
            if cell[(x,y)][0] == -1 and cell[(x,y)][1] == live:
                # 활성상태로 전환
                cell[(x,y)][0] = 1
                # 현재 진행도를 0으로 초기화
                cell[(x,y)][1] = 0

            # 세포 분열 가능하면 세포 분열
            # 세포가 활성 상태이며 1만큼 진행했을 시
            if cell[(x,y)][0] == 1 and cell[(x,y)][1] == 1:
                # 사방 탐색
                for dx,dy in dir:
                    px,py = x+dx,y+dy
                    # 탐색한 칸이 0이고 아무것도 없는 셀이라면
                    if arr[py][px] == 0:
                        if cell.get((px,py)) is None:
                            # 해당 칸에 분열
                            arr[py][px] = live
                            # cell dict에 해당 세포 정보 추가
                            cell[(px,py)] = [-1,0,live]
                        # 해당 칸에 다른 세포가 이번 타임에 번식했을 때
                        elif cell[(px,py)][0] == -1 and cell[(px,py)][1] == 0:
                            # 살아있을 수 있는 시간이 더 길다면
                            if arr[py][px] < live:
                                # 해당 칸에 분열
                                arr[py][px] = live
                                # cell dict에 해당 세포 정보를 덮어 씌움
                                cell[(px, py)] = [-1, 0, live]

            # 죽어야 할 세포 선정
            # 현재 활성 상태이며, 세포 진행도가 최대 수명과 같을 시 -> 세포 죽음
            if cell[(x,y)][0] == 1 and cell[(x,y)][1] == live:
                # cell dict에서 빼줌
                cell.pop((x,y))

    print("#{} {}".format(test,len(cell)))