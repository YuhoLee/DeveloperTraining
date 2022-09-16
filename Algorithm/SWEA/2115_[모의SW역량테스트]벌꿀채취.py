from itertools import product,combinations

t = int(input())
for test in range(1,t+1):
    n,m,c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    res = 0

    point = list(product(range(n),range(n-m+1)))
    comb = list(combinations(point,2))
    for bb1,bb2 in comb:
        y1,x1 = bb1
        y2,x2 = bb2
        if y1 == y2 and x1 < x2 < x1+m:
            continue
        combo1,combo2 = [],[]
        b1,b2 = 0,0
        for i in range(1,m+1):
            combo1 += combinations(arr[y1][x1:x1+m],i)
            combo2 += combinations(arr[y2][x2:x2+m],i)
        for i in range(len(combo1)):
            s1 = sum(combo1[i])
            if s1 <= c:
                d = sum(a**2 for a in combo1[i])
                if b1 < d:
                    b1 = d
            s2 = sum(combo2[i])
            if s2 <= c:
                d = sum(a**2 for a in combo2[i])
                if b2 < d:
                    b2 = d

        ss = b1+b2
        if res < ss: res = ss

    print("#{} {}".format(test,res))