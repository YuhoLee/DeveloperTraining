from collections import deque
for t in range(1,11):
    n, s = map(int, input().split())
    contact = list(map(int, input().split()))
    m = max(contact)+1
    arr = [[0]*m for _ in range(m)]
    visited = [False]*m
    for i in range(0,len(contact),2):
        arr[contact[i]][contact[i+1]] = 1
    res = 0
    q = deque()
    q.append(s)
    visited[s] = 1
    last = 1

    while q:
        node = q.popleft()
        last = visited[node]
        if res < node: res = node
        for i in range(m):
            if arr[node][i] != 0 and not visited[i]:
                q.append(i)
                visited[i] = visited[node]+1
    res = []
    for i in range(m):
        if visited[i] == last:
            res.append(i)
    print("#{} {}".format(t,max(res)))