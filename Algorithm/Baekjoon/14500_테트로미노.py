# 각 조각의 모양 별 가질 수 있는 경우의 수 -> 19가지
# 중심이 되는 (0,0)은 공통으로 가지고 있기에 따로 넣어주지 않음
# 사실 모양 구분 안하고 shapeList에 전부 넣은채로 돌려도 상관은 없지만 코드 가독성을 위해 다음과 같이 작성
IShape = [[(1,0),(2,0),(3,0)],[(0,1),(0,2),(0,3)]]
OShape = [[(0,1),(1,0),(1,1)]]
LShape = [[(0,1),(0,2),(1,2)],[(0,1),(0,2),(-1,2)],[(0,1),(1,0),(2,0)],[(1,0),(2,0),(2,1)],
          [(1,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(0,1),(1,1),(2,1)],[(0,1),(-1,1),(-2,1)]]
ZShape = [[(0,1),(1,1),(1,2)],[(0,1),(-1,1),(-1,2)],[(1,0),(1,1),(2,1)],[(1,0),(0,1),(-1,1)]]
TShape = [[(0,1),(-1,1),(1,1)],[(0,1),(-1,1),(0,2)],[(0,1),(1,1),(0,2)],[(1,0),(1,1),(2,0)]]
shapeList = [IShape, OShape, LShape, ZShape, TShape]

# init
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
buff = [a[:] for a in arr]
res = 0

# 전체 좌표에 대해
for i in range(n):
    for j in range(m):
        # shapeList에서 shape을 가져옴
        for shape in shapeList:
            # 해당 shape이 가질 수 있는 모든 모양을 가져옴
            for tiles in shape:
                # 현재 좌표는 도형의 중심이기에 무조건 있어야 하므로 처음에 더해줌
                total = arr[i][j]
                # 좌표칸을 벗어났는가에 대한 flag
                flag = True
                # 블럭 한 칸씩
                for dx,dy in tiles:
                    px,py = j+dx,i+dy
                    # 범위 벗어났을 시 flag False 후 탈출
                    if not(0 <= px < m and 0 <= py < n):
                        flag = False
                        break
                    # 범위 벗어나지 않았다면 해당 타일의 값을 total에 더해줌
                    total += arr[py][px]
                # 모양이 완성되었을 시 (모든 타일 칸이 범위를 벗어나지 않음)
                if flag:
                    # 최댓값 최신화
                    if res < total:
                        res = total
print(res)