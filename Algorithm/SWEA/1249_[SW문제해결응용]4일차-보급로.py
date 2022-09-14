t = int(input())
for test in range(1,t+1):
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(n):
            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                px,py = j+dx,i+dy
                if not(0 <= px < n and 0 <= py < n):
                    continue
                dp[py][px] = min(dp[py][px], dp[i][j]+arr[py][px])

    print("#{} {}".format(test, dp[n-1][n-1]))


