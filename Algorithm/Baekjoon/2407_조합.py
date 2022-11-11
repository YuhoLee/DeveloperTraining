n,m = map(int, input().split())
if m > n-m: m = n-m
res = 1
for i in range(n,n-m,-1):
    res *= i

for i in range(m,0,-1):
    res //= i

print(res)