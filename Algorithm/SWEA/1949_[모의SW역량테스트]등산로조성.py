def DFS(x, y, c):
    global res
    flag = False
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        xx, yy = x + dx, y + dy
        if 0 <= xx < n and 0 <= yy < n:
            if arr[y][x] > arr[yy][xx] and not visited[yy][xx]:
                flag = True
                visited[yy][xx] = True
                DFS(xx, yy, c + 1)
                visited[yy][xx] = False
    if not flag:
        if res < c: res = c


t = int(input())
for test in range(1, t + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for p in range(1, k + 1):
        for q in range(n):
            for r in range(n):
                m = 0
                for a in arr:
                    m = max(m, max(a))
                point = []
                for i in range(n):
                    for j in range(n):
                        if arr[i][j] == m:
                            point.append((j, i))
                arr[q][r] -= p
                for px, py in point:
                    visited = [[False] * n for _ in range(n)]
                    DFS(px, py, 1)
                arr[q][r] += p

    print("#{} {}".format(test, res))