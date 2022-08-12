t = int(input())
for test in range(1,t+1):
    n = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    arr.insert(0,[0]*(n+2))
    arr.append([0]*(n+2))
    visited = [[False]*(n+2) for _ in range(n+2)]
    res_list = []

    for i in range(1,n+1):
        for j in range(1,n+1):
            if not visited[i][j] and arr[i][j] != 0:
                x,y = j,i
                while arr[y][x+1] != 0:
                    x += 1
                while arr[y+1][x] != 0:
                    y += 1

                dx,dy = x-j+1,y-i+1
                res_list.append((dy,dx,dy*dx))
                for py in range(i,y+1):
                    for px in range(j,x+1):
                        visited[py][px] = True

    res_list.sort(key = lambda x: (x[2],x[0]))

    s = ''
    s += (str(len(res_list))+' ')
    for res in res_list:
        s += (str(res[0]) + ' ')
        s += (str(res[1]) + ' ')

    print("#{} {}".format(test, s))