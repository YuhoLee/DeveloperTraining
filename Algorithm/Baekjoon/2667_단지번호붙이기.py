def DFS(y,x):
    global cnt
    if arr[y][x] == 0:
        return
    else:
        if not visited[y][x]:
            visited[y][x] = True
            cnt += 1
            for i in range(4):
                DFS(y+dir[i][0],x+dir[i][1])

n = int(input())
arr = [[0] + list(map(int, input())) + [0] for _ in range(n)]
arr.insert(0,[0]*(n+2))
arr.append([0]*(n+2))
visited = [[False]*(n+2) for _ in range(n+2)]
dir = [[0,-1],[0,1],[-1,0],[1,0]]
cnt = 0
answer = []
for i in range(1,n+1):
    for j in range(1,n+1):
        cnt = 0
        DFS(i,j)
        if cnt != 0:
            answer.append(cnt)
answer.sort()
print(len(answer))
for a in answer:
    print(a)