n,m = int(input()),int(input())
graph = [[float('inf')]*n for _ in range(n)]
for _ in range(m):
    s,e,w = map(int, input().split())
    s,e = s-1,e-1
    graph[s][e] = min(graph[s][e], w)

for i in range(n):
    graph[i][i] = 0

for p in range(n):
    for i in range(n):
        if p != i:
            for j in range(n):
                if i != j and p != j:
                    graph[i][j] = min(graph[i][j], graph[i][p]+graph[p][j])

for gra in graph:
    for g in gra:
        if g != float('inf'):
            print(g,end=' ')
        else: print(0,end=' ')
    print()