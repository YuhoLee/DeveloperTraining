from collections import deque
import sys
input = sys.stdin.readline
dir = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]


n,m,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
soil = [[5]*n for _ in range(n)]
trees = {}
for i in range(n):
    for j in range(n):
        trees[(i,j)] = deque()
for _ in range(m):
    x,y,o = map(int, input().split())
    trees[(x-1,y-1)].appendleft(o)


for _ in range(k):
    for (i,j),tree_queue in trees.items():
        new_trees = deque()
        po = 0
        while tree_queue:
            old = tree_queue.pop()
            if soil[i][j] >= old:
                soil[i][j] -= old
                new_trees.appendleft(old + 1)
            else:
                po += (old//2)
        trees[(i, j)] = new_trees
        soil[i][j] += po

    for (i, j), tree_queue in trees.items():
        tree = list(tree_queue)
        for old in tree:
            if old % 5 == 0:
                for dx,dy in dir:
                    px,py = i+dx,j+dy
                    if 0 <= px < n and 0 <= py < n:
                        trees[(px,py)].append(1)
    for i in range(n):
        for j in range(n):
            soil[i][j] += arr[i][j]

res = 0
for i in range(n):
    for j in range(n):
        res += len(trees[(i,j)])
print(res)