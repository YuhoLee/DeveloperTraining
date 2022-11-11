from collections import deque


def bfs(x):
    if x == k: return 0
    visited = [False]*100001
    visited[x] = True
    q = deque()
    q.append((x,0))
    while q:
        x,c = q.popleft()
        if x == k:
            return c
        for pos in [x*2,x-1,x+1]:
            if 0 <= pos <= 100000 and not visited[pos]:
                visited[pos] = True
                if pos == x*2:
                    q.append((pos,c))
                else:
                    q.append((pos,c+1))


n,k = map(int, input().split())
res = bfs(n)
print(res)
