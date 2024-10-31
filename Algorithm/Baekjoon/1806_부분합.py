n,s = tuple(map(int, input().split()))
numList = list(map(int, input().split()))

start, end = 0, 0
res = n+1
total = numList[start]
while True:
    if total >= s:
        res = min(res, end-start+1)
        total -= numList[start]
        start += 1
    else:
        end += 1
        if end == n: break
        total += numList[end]

if res == n+1:
    print(0)
else:
    print(res)

