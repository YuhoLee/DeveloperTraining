# # Floyd Warshall
# t = int(input())
# for test in range(1,t+1):
#     arr = list(map(int, input().split()))
#     n = arr.pop(0)
#     network = [[0]*(n+1)]
#     for i in range(0,n*n,n):
#         network.append([0]+arr[i:i+n])
#
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if network[i][j] == 0:
#                 network[i][j] = float('inf')
#
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if i == j: continue
#             for k in range(1,n+1):
#                 if i == k or j == k: continue
#                 network[i][k] = min(network[i][k], network[i][j]+network[j][k])
#
#     res = float('inf')
#     for i in range(1,n+1):
#         ss = 0
#         for j in range(1,n+1):
#             if network[i][j] != float('inf'):
#                 ss += network[i][j]
#         if res > ss: res = ss
#
#     print("#{} {}".format(test, res))


from collections import deque


def BFS(s):
    global res
    q = deque()
    visited = [False]*n
    shortest_dis[s][s] = 0
    q.append((s,1))
    visited[s] = True
    while q:
        p,c = q.popleft()
        if sum(shortest_dis[s]) > res:
            break
        for i in range(n):
            if p == i: continue
            if not visited[i] and network[p][i]:
                q.append((i,c+1))
                visited[p] = True
                if shortest_dis[s][i] == 0:
                    shortest_dis[s][i] = c
                    shortest_dis[i][s] = c
    return sum(shortest_dis[s])


t = int(input())
for test in range(1,t+1):
    arr = list(map(int, input().split()))
    n = arr[0]
    network = []
    distance = [0] * n
    index = 1

    for i in range(n):
        buff = []
        for j in range(n):
            buff.append(arr[index])
            index += 1
        network.append(buff)

    shortest_dis = [[0]*n for _ in range(n)]
    res = 10**9
    for i in range(n):
        distance[i] = BFS(i)
        res = min(res,distance[i])

    print("#{} {}".format(test,res))
