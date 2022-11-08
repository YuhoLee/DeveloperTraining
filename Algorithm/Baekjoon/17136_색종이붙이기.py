def dfs(x, y, cnt):
    global res
    # y가 10에 도달 -> 모든 칸 탐색 했으므로 종료
    if y == 10:
        res = min(res, cnt)
        return
    # x가 10에 도달 -> 다음 행으로 이동
    if x == 10:
        dfs(0, y + 1, cnt)
        return
    # 해당 칸이 채워야 하는 부분이라면
    if arr[y][x]:
        # 1칸짜리 ~ 5칸짜리, p는 증가량
        for p in range(5):
            # 이미 5장을 사용 했다면 넘어감
            if paper[p] == 5:
                continue
            # 해당 색종이 사용 시 칸을 벗어난다면 넘어감
            if x + p >= 10 or y + p >= 10:
                continue

            # 해당 색종이를 사용 할 수 있는지
            # 즉, 색종이의 범위가 모두 1인지 확인
            rec = 0
            for i in range(y,y+p+1):
                rec += sum(arr[i][x:x+p+1])

            # 해당 색종이가 들어갈 수 있는 칸이라면
            if rec == (p+1)*(p+1):
                # 해당 범위를 모두 채움
                for i in range(y,y+p+1):
                    for j in range(x,x+p+1):
                        arr[i][j] = 0
                # 사용한 색종이 수를 1 증가
                paper[p] += 1
                # 현재 상태를 기준으로 다음 칸으로 이동하여 계속 채우기 실행
                dfs(x + p + 1, y, cnt + 1)

                # 다음 케이스를 위해 원래대로 돌려놓음
                paper[p] -= 1
                for i in range(y, y + p + 1):
                    for j in range(x, x + p + 1):
                        arr[i][j] = 1

    # 채워야 하는 부분이 아니면 다음 칸으로 이동
    else:
        dfs(x + 1, y, cnt)


# init
arr = [list(map(int, input().split())) for _ in range(10)]
paper = [0, 0, 0, 0, 0]
res = float('inf')
dfs(0, 0, 0)
if res == float('inf'):
    print(-1)
else:
    print(res)