def dfs(c):
    global find
    if c == end:
        find = True
        return
    for i in range(n+1):
        if not find:
            if c != i and graph[c][i] and not visited[i]:
                visited[i] = True
                path.append(i)
                dfs(i)
                if not find:
                    visited[i] = False
                    path.pop(-1)
        else: break


n = int(input())
circle = [list(map(int, input().split())) for _ in range(n)]
start, end = map(int, input().split())
circle.sort(key = lambda a: a[2])
circle = [None] + circle
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
path = []
find = False
for i in range(1,n+1):
    for j in range(i,n+1):
        if i != j:
            d = abs(circle[i][1] - circle[j][1])
            rr = circle[i][2] - circle[j][2]
            if abs(rr) > d:
                if rr < 0:
                    graph[circle[i][0]][circle[j][0]] = 1
                else:
                    graph[circle[j][0]][circle[i][0]] = 1
for i in range(1,n+1):
    if sum(graph[i]) == 0:
        graph[i][0] = 1
for i in range(0,n+1):
    for j in range(0,n+1):
        if graph[i][j] == 1:
            graph[j][i] = 1

visited[start] = True
path.append(start)
dfs(start)
print(len(path))
print(' '.join(map(str,path)))