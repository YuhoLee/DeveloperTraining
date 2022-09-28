attack_dir = [[],[0,-1],[0,1],[-1,0],[1,0]]
dir = [[-1,0],[0,1],[1,0],[0,-1]]


def dir_func(i):
    return (i+1)%4


# 블리자드로 구슬 파괴
def break_biz(d,s):
    ddx, ddy = 0, 0
    for _ in range(s):
        ddx, ddy = ddx + attack_dir[d][0], ddy + attack_dir[d][1]
        bx, by = shark_x + ddx, shark_y + ddy
        arr[by][bx] = -1


def list_map():
    merge_list = []
    x, y = shark_x, shark_y
    visited = [[False] * n for _ in range(n)]
    d = 3
    for i in range(n ** 2):
        visited[y][x] = True
        merge_list.append(arr[y][x])
        next_dir = dir[(d + 1) % 4]
        if not visited[y + next_dir[1]][x + next_dir[0]]:
            d = (d + 1) % 4
        dx, dy = dir[d]
        x, y = x + dx, y + dy
    return merge_list


# 빈 자리 구슬 밀어주기
def move_biz():
    move_list = [0]*(n**2)
    idx = 0
    for i in range(n**2):
        if merge_list[i] != -1:
            move_list[idx] = merge_list[i]
            idx += 1
    return move_list


# 구슬 폭발
def explosion_biz():
    global score
    flag = False
    cnt,start,biz = 0,0,0

    for i in range(1,len(merge_list)):
        if merge_list[i] == merge_list[start]:
            cnt += 1
        else:
            if cnt >= 4:
                for idx in range(start,i):
                    merge_list[idx] = -1
                score += (biz * cnt)
                flag = True
            cnt, start, biz = 1,i,merge_list[i]
    return flag


# 구슬 증식
def increase_biz():
    if len(merge_list) == 1:
        return merge_list
    new_merge = [0]
    flag = False
    s, start = 1, 0
    for idx in range(1,len(merge_list)-1):
        next_idx = idx + 1
        if merge_list[idx] == merge_list[next_idx]:
            if not flag:
                flag = True
            s += 1
        else:
            obj = merge_list[idx]
            if flag:
                new_merge.append(s)
                s = 1
                flag = False
            else:
                new_merge.append(1)
            new_merge.append(obj)
        idx += 1
    if merge_list[-1] != merge_list[-2]:
        new_merge.append(1)
        new_merge.append(merge_list[-1])
    return new_merge[:n*n]


def list_to_batch(merge):
    global arr
    x, y = shark_x, shark_y
    visited = [[False] * n for _ in range(n)]
    arr = [[0] * n for _ in range(n)]
    d = 3
    for i in range(len(merge)):
        visited[y][x] = True
        arr[y][x] = merge[i]
        next_dir = dir[(d + 1) % 4]
        if not visited[y + next_dir[1]][x + next_dir[0]]:
            d = (d + 1) % 4
        dx, dy = dir[d]
        x, y = x + dx, y + dy


n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
blizzard = [list(map(int, input().split())) for _ in range(m)]
shark_x,shark_y = n//2,n//2
score = 0

for d,ss in blizzard:
    break_biz(d,ss)
    merge_list = list_map()
    merge_list = move_biz()
    while explosion_biz():
        merge_list = move_biz()
    merge_list = increase_biz()
    list_to_batch(merge_list)
print(score)