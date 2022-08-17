from itertools import product
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
t_arr = list(list(zip(*arr)))
dir = ['left','right','up','down']

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


n_max = 0
for case in product([0,1,2,3],repeat=5):
    tmp = [cp[:] for cp in arr]

    for s in case:
        play(dir[s])
        if dir[s] in ['up','down']:
            arr = list(map(list, zip(*t_arr)))
        else:
            t_arr = list(map(list, zip(*arr)))
        for a in arr:
            for t in a:
                if t > n_max: n_max = t

    arr = tmp
    t_arr = list(list(zip(*arr)))
print(n_max)