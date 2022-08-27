from itertools import permutations

def hunt(order):
    global min_distance
    huntList = []
    hunter = (0,0)
    dis = 0
    for ord in order:
        if ord < 0:
            if -ord not in huntList: return
            else:
                oy, ox = customer[-ord]
                dis += (abs(oy - hunter[0]) + abs(ox - hunter[1]))
                hunter = customer[-ord]
        elif ord > 0:
            huntList.append(ord)
            my, mx = monster[ord]
            dis += (abs(my-hunter[0]) + abs(mx-hunter[1]))
            hunter = monster[ord]
    if min_distance > dis: min_distance = dis

t = int(input())
for test in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mc = []
    monster, customer = [0]*5,[0]*5
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                mc.append(arr[i][j])
                if arr[i][j] > 0: monster[arr[i][j]] = (i,j)
                else: customer[-arr[i][j]] = (i,j)
    min_distance = float('inf')
    case = list(permutations(mc,len(mc)))
    for c in case:
        hunt(c)
    print("#{} {}".format(test, min_distance))