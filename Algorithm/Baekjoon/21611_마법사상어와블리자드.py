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
        arr[by][bx] = 0


# 빈 자리 구슬 밀어주기
def move_biz():
    global arr
    merge_list = []
    x, y = shark_x, shark_y
    visited = [[False] * n for _ in range(n)]
    d = 3
    for i in range(n ** 2):
        visited[y][x] = True
        if i == 0 or arr[y][x] != 0:
            merge_list.append(arr[y][x])
        next_dir = dir[(d + 1) % 4]
        if not visited[y + next_dir[1]][x + next_dir[0]]:
            d = (d + 1) % 4
        dx, dy = dir[d]
        x, y = x + dx, y + dy
    return merge_list


# 구슬 폭발
def explosion_biz():
    global arr,merge_list,score
    if len(merge_list) == 1: return
    trigger = True
    while trigger:
        trigger = False
        flag = False
        s,start = 1,0
        new_merge = []
        for idx in range(len(merge_list)-1):
            next_idx = idx+1
            if merge_list[idx] == merge_list[next_idx]:
                if not flag:
                    flag = True
                    start = idx
                s += 1
            else:
                if flag:
                    if s >= 4:
                        trigger = True
                        obj = merge_list[idx]
                        score[obj-1] += obj * s
                    else:
                        for i in range(start,idx+1):
                            new_merge.append(merge_list[i])
                    s = 1
                    flag = False
                else:
                    new_merge.append(merge_list[idx])
        if len(merge_list) == 1: break
        if merge_list[-1] != merge_list[-2]:
            new_merge.append(merge_list[-1])
        if flag and s >= 4:
            obj = merge_list[idx]
            score[obj - 1] += obj * s
        elif flag and s < 4:
            for i in range(start, idx + 2):
                new_merge.append(merge_list[i])
        merge_list = new_merge


# 구슬 증식
def increase_biz():
    if len(merge_list) == 1: return merge_list
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
score = [0,0,0]

for d,ss in blizzard:
    break_biz(d,ss)
    merge_list = move_biz()
    explosion_biz()
    merge_list = increase_biz()
    list_to_batch(merge_list)
print(sum(score))