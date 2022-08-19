# from collections import deque
# # 2번째 인덱스는 가로, 세로, 대각선에 대한 정보
# # 0: 가로, 1: 세로, 2: 대각선
# r_dir = [[1,0,0],[1,1,2]]
# c_dir = [[0,1,1],[1,1,2]]
# x_dir = [[1,0,0],[0,1,1],[1,1,2]]
# dir = [r_dir,c_dir,x_dir]
#
#
# def BFS():
#     res = 0
#     q = deque()
#     q.append((1,0,0))
#     while q:
#         x,y,s = q.popleft()
#         if x == n-1 and y == n-1: res += 1
#         for dx,dy,ds in dir[s]:
#             px, py = x + dx, y + dy
#             if 0 <= px < n and 0 <= py < n:
#                 if arr[py][x] + arr[y][px] + arr[py][px] == 0:
#                     q.append((px,py,ds))
#     return res
#
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# print(BFS())



# def DFS(x,y,s):
#     res = 0
#     if x == n-1 and y == n-1: res += 1
#     for dx, dy, ds in dir[s]:
#         px, py = x + dx, y + dy
#         if not(0 <= px < n and 0 <= py < n): continue
#         if arr[py][x] + arr[y][px] + arr[py][px] == 0:
#             res += DFS(px,py,ds)
#     return res
#
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dir = [[[1,0,0],[1,1,2]],[[0,1,1],[1,1,2]],[[1,0,0],[0,1,1],[1,1,2]]]
# print(DFS(1,0,0))

# BFS, DFS 안 풀려서 DP 활용...

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*n for i in range(n)] for j in range(3)]
dp[0][0][1] = 1

for i in range(2,n):
    if arr[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1,n):
    for j in range(1,n):
        if arr[i-1][j] + arr[i][j-1] + arr[i][j] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        if arr[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
print(sum([dp[i][n-1][n-1] for i in range(3)]))
