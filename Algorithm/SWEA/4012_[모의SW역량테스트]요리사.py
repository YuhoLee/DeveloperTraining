from itertools import combinations
t = int(input())
for test in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    comb = list(combinations(range(n),n//2))
    l = len(comb)
    res = float('inf')

    for i in range(l//2):
        combo1 = comb[i]
        combo2 = comb[-(i+1)]
        score1 = 0
        score2 = 0
        for i in range(n//2):
            for j in range(i+1,n//2):
                score1 += arr[combo1[i]][combo1[j]]
                score1 += arr[combo1[j]][combo1[i]]
                score2 += arr[combo2[i]][combo2[j]]
                score2 += arr[combo2[j]][combo2[i]]
        val = abs(score1 - score2)
        if res > val: res = val
    print("#{} {}".format(test,res))