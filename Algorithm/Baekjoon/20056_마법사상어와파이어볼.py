import copy


# 방향이 모두 홀수나 짝수인지 검사하는 함수
def check_all_odd_or_even(y,x):
    odd_flag = False
    even_flag = False
    target = arr[y][x]

    # 홀짝 검사
    for _,_,d in target:
        if d % 2 == 0:
            even_flag = True
        else:
            odd_flag = True

    # 홀,짝 둘 다 존재하는지 확인
    if odd_flag and even_flag:
        return False
    else:
        return True


# 파이어볼 move 함수
def move():
    global arr
    buff = [[[] for _ in range(n)] for _ in range(n)]
    # 전체에 대해서
    for i in range(n):
        for j in range(n):
            # 파이어볼이 있다면
            if len(arr[i][j]) != 0:
                # 해당 칸의 파이어볼들에 대해 가진 속도 및 방향만큼 이동시킴
                for m, s, d in arr[i][j]:
                    dx, dy = dir[d]
                    px = (j + dx * s) % n
                    py = (i + dy * s) % n
                    buff[py][px].append([m, s, d])
    # buff 복사
    arr = copy.deepcopy(buff)


# 합쳐진 후 분열하는 함수
def lump_divide():
    global arr
    buff = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 파이어볼이 1개보다 많이 있다면
            if len(arr[i][j]) > 1:
                # 해당 칸의 파이어볼 개수, 분열 시 질량, 분열 시 속도를 구함
                tl = len(arr[i][j])
                tm = sum([m for m,_,_ in arr[i][j]]) // 5
                ts = sum([s for _,s,_ in arr[i][j]]) // tl
                # tm이 0이 아니라면 -> 어차피 0은 사라지기 때문에
                if tm > 0:
                    # 모든 방향이 홀 또는 짝이라면
                    if check_all_odd_or_even(i,j):
                        # 짝수 방향
                        for rd in range(0,8,2):
                            buff[i][j].append([tm,ts,rd])
                    else:
                        # 홀수 방향
                        for rd in range(1,8,2):
                            buff[i][j].append([tm, ts, rd])
            elif len(arr[i][j]) == 1:
                buff[i][j].append(arr[i][j][0])

    # buff 복사
    arr = copy.deepcopy(buff)


# init
n, m, k = map(int, input().split())
dir = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
arr = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])

for _ in range(k):
    move()
    lump_divide()

# 전체 질량을 구함
res = 0
for i in range(n):
    for j in range(n):
        if len(arr[i][j]) != 0:
            for m,_,_ in arr[i][j]:
                res += m
print(res)
