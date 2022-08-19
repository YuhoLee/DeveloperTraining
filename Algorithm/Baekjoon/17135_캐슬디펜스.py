from itertools import combinations

h,w,d = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(h)]

if d == 1:
    t_arr = list(list(zip(*tmp)))
    m = [sum(a) for a in t_arr]
    m.sort(reverse=True)
    print(sum(m[:3]))
else:
    mm = 0
    res = 0
    for i in range(h):
        for j in range(w):
            if tmp[i][j] == 1: mm += 1

    for a1,a2,a3 in combinations(range(w),3):
        arr = [t[:] for t in tmp]
        archer = [(h,a1),(h,a2),(h,a3)]
        hit = 0
        monster = mm
        while monster > 0:
            shoot = [False]*3
            visited = [[False] * w for _ in range(h)]
            for j, (y, x) in enumerate(archer):
                success = False
                if not shoot[j]:
                    for dd in range(1,d+1):
                        for i in range(-dd+1,dd):
                            px = x+i
                            if i <= 0: i *= -1
                            py = y-dd+i
                            if 0 <= px < w and 0 <= py < h:
                                if arr[py][px] == 1:
                                    visited[py][px] = True
                                    shoot[j] = True
                                    success = True
                                    break
                        if success: break
            for r in range(h):
                for c in range(w):
                    if visited[r][c]:
                        arr[r][c] = 0
                        hit += 1
                        monster -= 1

            for ar in arr[h-1]:
                if ar == 1: monster -= 1
            for i in range(h-2,-1,-1):
                for j in range(w):
                    arr[i+1][j] = arr[i][j]
            arr[0] = [0]*w
        if res < hit: res = hit

    print(res)
