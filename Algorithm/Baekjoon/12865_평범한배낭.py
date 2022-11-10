n,k = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]
bag.insert(0,[0,0])
dp = [[0]*(n+1) for _ in range(k+1)]

for i in range(1,n+1):
    for w in range(1,k+1):
        if w - bag[i][0] >= 0:
            dp[w][i] = max(dp[w][i-1],dp[w-bag[i][0]][i-1]+bag[i][1])
        else:
            dp[w][i] = dp[w][i-1]

print(dp[k][n])