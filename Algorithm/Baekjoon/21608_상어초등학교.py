# init
n = int(input())
std_num = n**2
favor_list = []
std_state = [0] + [False] * std_num
arr = [[0]*n for j in range(n)]
favor_list = [list(map(int, input().split())) for _ in range(n)]

for favor in favor_list:
    std = favor[0]
    favor_std = []
    for c in favor[1:]:
        if std_state[c]: favor_std.append(c)

    cnt_arr = []
    # 1순위: 선호하는 학생 수가 많을수록
    # 2순위: 빈 칸이 많을수록
    # 3순위: 좌표 행 작을수록
    # 4순위: 좌표 열 작을수록
    for i in range(n):
        for j in range(n):
            empty_num, favor_num = 4,4
            if arr[i][j] == 0:
                for k in [(-1,0),(1,0),(0,-1),(0,1)]:
                    x = i + k[0]
                    y = j + k[1]
                    if 0 <= x < n and 0 <= y < n:
                        if arr[x][y] == 0:
                            empty_num += 1
                        elif arr[x][y] in favor_std:
                            favor_num += 1
                cnt_arr.append([(i, j), favor_num, empty_num])
            else:
                cnt_arr.append([(n,n), -1, -1])
    cnt_arr.sort(key=lambda x: (x[1], x[2], -x[0][0], -x[0][1]))
    best = cnt_arr[-1]
    std_state[std] = (best[0][0], best[0][1])
    arr[best[0][0]][best[0][1]] = std

point = 0
for favor in favor_list:
    std = favor[0]
    px = std_state[std][0]
    py = std_state[std][1]
    sub = 0
    for k in [(-1,0),(1,0),(0,-1),(0,1)]:
        x = px + k[0]
        y = py + k[1]
        # 전체에 대한 포인트 계산
        if 0<=x<n and 0<=y<n and arr[x][y] in favor[1:]:
            sub += 1
    if sub == 1: point += 1
    elif sub == 2: point += 10
    elif sub == 3: point += 100
    elif sub == 4: point += 1000
print(point)