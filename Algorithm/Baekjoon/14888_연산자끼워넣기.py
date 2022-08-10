def DFS(res, c, s1, s2, s3, s4):
    global max_num, min_num
    c += 1
    if sum([s1,s2,s3,s4]) == 0:
        if max_num < res: max_num = res
        if min_num > res: min_num = res
        return
    else:
        if s1 != 0:
            DFS(res+num[c], c, s1-1, s2, s3, s4)
        if s2 != 0:
            DFS(res-num[c], c, s1, s2-1, s3, s4)
        if s3 != 0:
            DFS(res*num[c], c, s1, s2, s3-1, s4)
        if s4 != 0:
            if res < 0:
                res *= (-1)
                DFS(-(res // num[c]), c, s1, s2, s3, s4 - 1)
            else:
                DFS(res // num[c], c, s1, s2, s3, s4 - 1)

n = int(input())
num = list(map(int, input().split()))
state = list(map(int, input().split()))
res = num[0]
max_num = float("-inf")
min_num = float("inf")
DFS(res, 0, state[0], state[1], state[2], state[3])
print(max_num)
print(min_num)
