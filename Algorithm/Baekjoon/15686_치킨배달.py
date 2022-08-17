from itertools import combinations

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chicken = []
home = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((j,i))
        if arr[i][j] == 2:
            chicken.append((j,i))

res = float('inf')
for ch in combinations(chicken,m):
    dis = 0
    for hx, hy in home:
        total = 0
        hh = []
        for cx, cy in ch:
            hh.append(abs(cx-hx)+abs(cy-hy))
        dis += min(hh)
    if res > dis: res = dis

print(res)