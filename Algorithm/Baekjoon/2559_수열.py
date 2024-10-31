n,k = tuple(map(int, input().split()))
temps = list(map(int, input().split()))

res = -100 * 100000
total = 0
for i in range(0,k-1):
    total += temps[i]

for i in range(k-1, n):
    total += temps[i]
    res = max(res, total)
    total -= temps[i-(k-1)]

print(res)