dict = {}
def DFS(total):
    global res
    l = len(matrix)
    if l == 1:
        if res > total: res = total
    for i in range(l-1):
        a,b = matrix[i],matrix[i+1]
        tt = a[0] * a[1] * b[1]
        matrix.pop(i)
        matrix.pop(i)
        matrix.insert(i,(a[0],b[1]))
        DFS(total+tt)
        matrix.pop(i)
        matrix.insert(i,b)
        matrix.insert(i,a)


t = int(input())
for test in range(1,t+1):
    n = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    arr.insert(0,[0]*(n+2))
    arr.append([0]*(n+2))
    visited = [[False]*(n+2) for _ in range(n+2)]
    matrix = []
    res = float('inf')

    for i in range(1,n+1):
        for j in range(1,n+1):
            if not visited[i][j] and arr[i][j] != 0:
                x,y = j,i
                while arr[y][x+1] != 0:
                    x += 1
                while arr[y+1][x] != 0:
                    y += 1

                dx,dy = x-j+1,y-i+1
                matrix.append((dy,dx))
                for py in range(i,y+1):
                    for px in range(j,x+1):
                        visited[py][px] = True
    matrix.sort(key = lambda x: (x[0],x[1]))

    print("#{} {}".format(test,res))
