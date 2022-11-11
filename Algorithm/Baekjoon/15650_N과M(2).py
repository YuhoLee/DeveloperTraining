from itertools import combinations

n,m = map(int, input().split())

for p in map(list,combinations(range(1,n+1),m)):
    print(' '.join(map(str, p)))

