from itertools import combinations
from collections import deque


def BFS(s):
    q = deque()
    start = s[0]
    pp = population[start]
    cc = 1
    q.append(start)
    visited[s[0]] = True
    while q:
        elem = q.popleft()
        for i in range(n+1):
            if not visited[i] and graph[elem][i] and i in s:
                q.append(i)
                visited[i] = True
                pp += population[i]
                cc += 1
    return pp, cc


n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i] = 1
    line = list(map(int, input().split()))
    for l in line[1:]:
        graph[i][l] = 1
        graph[l][i] = 1
case = []
for i in range(1,n):
    case += combinations(range(1,n+1),i)

p = len(case) // 2
res = float('inf')
for i in range(p):
    visited = [False]*(n+1)
    per1,c1 = BFS(case[i])
    per2,c2 = BFS(case[(i+1)*(-1)])
    if c1+c2 == n:
        per = abs(per1-per2)
        if per < res: res = per
if res == float('inf'): print(-1)
else: print(res)