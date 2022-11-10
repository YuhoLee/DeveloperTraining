import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]: continue

        for nxt in arr[node]:
            cost = distance[node] + nxt[1]
            if cost < distance[nxt[0]]:
                distance[nxt[0]] = cost
                heapq.heappush(q, (cost, nxt[0]))


n,m,x = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,t = map(int, input().split())
    arr[s].append((e,t))

res = [0]*(n+1)

for i in range(1,n+1):
    distance = [float('inf')] * (n + 1)
    dijkstra(i)
    res[i] += distance[x]

distance = [float('inf')] * (n + 1)
dijkstra(x)
for i in range(1,n+1):
    res[i] += distance[i]

print(max(res))