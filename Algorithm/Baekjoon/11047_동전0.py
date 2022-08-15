import sys

n,k = tuple(map(int, sys.stdin.readline().split(' ')))
ml = []
for _ in range(n):
    ml.append(int(sys.stdin.readline()))
cnt = 0
for i in range(n-1,-1,-1):
    if k == 0: break
    else:
        if k >= ml[i]:
            q = k//ml[i]
            cnt += q
            k -= q * ml[i]
print(cnt)