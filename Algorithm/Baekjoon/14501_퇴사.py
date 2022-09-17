# DFS 수행
def consulting(idx,benefit):
    global res
    if idx == n and res < benefit:
        res = benefit
        return
    consulting(idx+consult[idx][0], benefit+consult[idx][1])
    consulting(idx+1,benefit)


# init
n = int(input())
consult = []
res = 0
for _ in range(n):
    consult.append(list(map(int,input().split())))

consulting(0,0)
print(res)