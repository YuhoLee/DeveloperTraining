# 3) DP 이용: 0-1 knapsack 알고리즘
testcase = int(input())
for test in range(testcase):
    n, k = tuple(map(int, input().split(' ')))
    food = [0] * (n + 1)
    for i in range(n):
        food[i] = list(map(int, input().split(' ')))
    food[n] = [0,0]
        # idx 0: 만족도, idx 1: 칼로리
    arr = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n+1):
        for j in range(k+1):
            if food[i][1] > j:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = max(food[i][0] + arr[i-1][j-food[i][1]], arr[i-1][j])

    print("#{0} {1}".format(test+1, arr[n][k]))




# 1) 모든 경우의 수를 다 도는 브루트포스
# 시간초과... 실패
# def hamburger(satis, kcal, v):
#     global n,l
#     global satisMax
#     for i in range(n):
#         if not visited[i]:
#             if kcal + foodList[i][1] > l:
#                 if satisMax < satis:
#                     satisMax = satis
#             else:
#                 visited[i] = True
#                 hamburger(satis + foodList[i][0], kcal + foodList[i][1])
#                 visited[i] = False
#
# testcase = int(input())
# for test in range(testcase):
#     n, l = tuple(map(int, input().split(' ')))
#     satisMax = 0
#     foodList = [0] * n
#     visited = [False] * n
#     for i in range(n):
#         foodList[i] = list(map(int, input().split(' ')))
#
#     hamburger(0,0,[False] * n)
#     print("#{0} {1}".format(test+1, satisMax))


# 2) DFS
# DFS 활용하여 성공
# def hamburger(idx, satis, kcal):
#     global n, l
#     global satisMax
#     if kcal > l: return
#     if idx == n:
#         if kcal <= l:
#             if satisMax < satis:
#                 satisMax = satis
#         return
#
#     hamburger(idx + 1, satis + food[idx][0], kcal + food[idx][1])
#     hamburger(idx + 1, satis, kcal)
#
#
# testcase = int(input())
# for test in range(testcase):
#     n, l = tuple(map(int, input().split(' ')))
#     satisMax = 0
#     food = [0] * n
#     for i in range(n):
#         food[i] = list(map(int, input().split(' ')))
#         # idx 0: 만족도, idx 1: 칼로리
#
#     hamburger(0, 0, 0)
#     print("#{0} {1}".format(test + 1, satisMax))