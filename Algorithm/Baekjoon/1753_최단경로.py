from heapq import heappop, heappush

v, e = map(int, input().split())
q = []
start = int(input()) - 1
graph = [[] for _ in range(v)]
cost = [float('inf')] * v
for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s - 1].append([w, e - 1])

cost[start] = 0

heappush(q,(cost[start], start))
while q:
    curr_dis, curr = heappop(q)
    if cost[curr] < curr_dis:
        continue
    for need, next in graph[curr]:
        if curr_dis + need < cost[next]:
            cost[next] = curr_dis + need
            heappush(q, [cost[next], next])

for i in range(v):
    if cost[i] != float('inf'):
        print(cost[i])
    else:
        print('INF')
