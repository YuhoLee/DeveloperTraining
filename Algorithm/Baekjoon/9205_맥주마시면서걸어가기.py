import sys
from queue import Queue

def calcDis(s, e):
    return abs(e[0]-s[0]) + abs(e[1]-s[1])

def BeerWalk():
    q = Queue()
    q.put(start)
    while not q.empty():
        spot = q.get()
        dis = calcDis(spot, end)
        if dis <= 1000: return 'happy'
        for i in range(len(conv)):
            if calcDis(spot, conv[i]) <= 1000 and not visited[i] :
                q.put(conv[i])
                visited[i] = True
    return 'sad'

t = int(sys.stdin.readline())
for _ in range(t):
    # 입력부
    n = int(sys.stdin.readline())
    conv = []
    start = tuple(map(int, sys.stdin.readline().split(' ')))
    for _ in range(n):
        conv.append(tuple(map(int, sys.stdin.readline().split())))
    end = tuple(map(int, sys.stdin.readline().split()))
    visited = [False for x in range(len(conv))]
    print(BeerWalk())

