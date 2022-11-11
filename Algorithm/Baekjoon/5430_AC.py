from collections import deque

test = int(input())
for t in range(test):
    isFront = True
    command = list(input())
    n = int(input())
    arr = input()
    if arr == "[]": arr = []
    else: arr = list(map(int, arr[1:len(arr)-1].split(',')))

    q = deque()

    for a in arr:
        q.append(a)

    flag = True
    for com in command:
        if com == "R":
            isFront = not isFront
        elif com == "D":
            if q:
                if isFront:
                    q.popleft()
                else:
                    q.pop()
            else:
                flag = False
                break
    if flag:
        if isFront:
            res = "[" + ','.join(list(map(str,list(q)))) + "]"
            print(res)
        else:
            res = "[" + ','.join(list(map(str,list(q)[::-1]))) + "]"
            print(res)
    else: print('error')

