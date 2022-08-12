t = int(input())
for test in range(1,t+1):
    n, m = map(int, input().split())
    num = []

    c = 1
    flag = True
    while n >= c:
        b = m % 2
        if b == 0:
            flag = False
            break
        m //= 2
        c += 1

    if flag: print("#{} ON".format(test))
    else: print("#{} OFF".format(test))