def visit(c, curr, dis):
    global res
    x,y = curr
    if dis > res:
        return
    if c == n:
        dis += (abs(hx-x) + abs(hy-y))
        if dis < res:
            res = dis
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            px,py = tp[i][0], tp[i][1]
            dd = abs(px-x) + abs(py-y)
            visit(c+1,tp[i],dis+dd)
            visited[i] = False


t = int(input())
for test in range(1,t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    sx,sy = arr[0],arr[1]
    hx,hy = arr[2],arr[3]
    tp = []
    visited = [False]*n
    for i in range(4,len(arr),2):
        tp.append((arr[i],arr[i+1]))
    res = float('inf')
    visit(0,(sx,sy), 0)
    print("#{} {}".format(test,res))
