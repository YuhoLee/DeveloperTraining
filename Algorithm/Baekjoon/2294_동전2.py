n,k = map(int, input().split())
dp = [float('inf')] * 100000
for _ in range(n):
    p = int(input())
    dp[p] = 1
m = min(dp)

for i in range(m+1,k+1):
    buff = dp[:i]
    dp[i] = min(dp[i], min([buff[t]+buff[-t] for t in range(1,i//2+1)]))

if dp[k] != float('inf'):
    print(dp[k])
else:
    print(-1)