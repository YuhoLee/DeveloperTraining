from collections import deque

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


class Point:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return "({0},{1})".format(self.y, self.x)

    def copy(self):
        return Point(self.y, self.x)


def DFS(prev, count):
    global virus_info, virus_buff, virus_case, m
    if count >= m:
        virus_case.append(virus_buff.copy())
    else:
        if len(virus_info) - prev < m - count: return
        for idx in range(prev + 1, len(virus_info)):
            v = virus_info[idx]
            if v not in virus_buff:
                virus_buff.append(v)
                DFS(idx, count + 1)
                virus_buff.pop(len(virus_buff) - 1)


def get_virus_case():
    global virus_buff, virus_case
    DFS(prev=-1, count=0)


def BFS():
    global n, virus_case

    return_res = float('inf')

    for case in virus_case:
        q = deque()
        lab = [[0] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        total = 0
        infect_count = 0
        compare_infect_count = 0

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    lab[i][j] = -1
                elif matrix[i][j] == 2:
                    lab[i][j] = -2
                else:
                    compare_infect_count +=1

        for vc in case:
            q.append([vc.y, vc.x, 0])
            lab[vc.y][vc.x] = -3
            visited[vc.y][vc.x] = True

        while q:
            vy, vx, count = q.popleft()
            for dy, dx in dir:
                ry, rx = vy + dy, vx + dx
                if not (0 <= ry < n and 0 <= rx < n): continue
                if (lab[ry][rx] == 0 or lab[ry][rx] == -2) and not visited[ry][rx]:
                    if lab[ry][rx] == 0:
                        infect_count += 1
                    lab[ry][rx] = count + 1
                    visited[ry][rx] = True
                    total = count + 1
                    q.append([ry, rx, count + 1])

            if compare_infect_count == infect_count:
                break

        if compare_infect_count == infect_count:
            return_res = min(return_res, total)

    return return_res


n, m = tuple(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(n)]

flag = True
for mrx in matrix:
    if 0 in mrx:
        flag = False

if flag:
    print(0)
else:
    virus_info = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 2:
                virus_info.append(Point(i, j))

    virus_buff = []
    virus_case = []
    get_virus_case()

    res = BFS()
    if res == float('inf'):
        res = -1
    print(res)
