test = int(input())
for t in range(1,test+1):
    n, s = tuple(input().split())
    n = int(n)
    arr = [list(map(int, input().split())) for _ in range(n)]
    t_arr = list(zip(*arr))

    def play(dir):
        if dir == 'left':
            for p,b in enumerate(arr):
                l = []
                nn = 0
                for s in b:
                    if s != 0:
                        l.append(s)
                        nn += 1
                buff = []
                i,c = 0,0
                while i < nn:
                    if i == nn-1:
                        buff.append(l[i])
                        break
                    if l[i] == l[i+1]:
                        buff.append(l[i]*2)
                        c += 1
                        i += 1
                    elif l[i] != 0: buff.append(l[i])
                    i += 1
                for _ in range(n-nn+c):
                    buff.append(0)
                arr[p] = buff

        elif dir == 'right':
            for p,b in enumerate(arr):
                l = []
                nn = 0
                for s in b:
                    if s != 0:
                        l.append(s)
                        nn += 1
                buff = []
                i,c = nn-1,0
                while i >= 0:
                    if i == 0:
                        buff.insert(0,l[i])
                        break
                    if l[i] == l[i-1]:
                        buff.insert(0,l[i]*2)
                        c += 1
                        i -= 1
                    elif l[i] != 0: buff.insert(0,l[i])
                    i -= 1
                for _ in range(n-nn+c):
                    buff.insert(0,0)
                arr[p] = buff
        elif dir ==  'up':
            for p,b in enumerate(t_arr):
                l = []
                nn = 0
                for s in b:
                    if s != 0:
                        l.append(s)
                        nn += 1
                buff = []
                i,c = 0,0
                while i < nn:
                    if i == nn-1:
                        buff.append(l[i])
                        break
                    if l[i] == l[i+1]:
                        buff.append(l[i]*2)
                        c += 1
                        i += 1
                    elif l[i] != 0: buff.append(l[i])
                    i += 1
                for _ in range(n-nn+c):
                    buff.append(0)
                t_arr[p] = buff
        elif dir == 'down':
            for p,b in enumerate(t_arr):
                l = []
                nn = 0
                for s in b:
                    if s != 0:
                        l.append(s)
                        nn += 1
                buff = []
                i,c = nn-1,0
                while i >= 0:
                    if i == 0:
                        buff.insert(0,l[i])
                        break
                    if l[i] == l[i-1]:
                        buff.insert(0,l[i]*2)
                        c += 1
                        i -= 1
                    elif l[i] != 0: buff.insert(0,l[i])
                    i -= 1
                for _ in range(n-nn+c):
                    buff.insert(0,0)
                t_arr[p] = buff

    play(s)
    if s in ['up','down']:
        arr = list(map(list, zip(*t_arr)))
    for i,a in enumerate(arr):
        arr[i] = ' '.join(map(str, a))

    print("#{}".format(t))
    for a in arr:
        print(a)
