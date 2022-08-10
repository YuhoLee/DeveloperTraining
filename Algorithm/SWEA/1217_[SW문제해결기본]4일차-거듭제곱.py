def power(a):
    global n, p, res
    if a == p:
        return
    else:
        res *= n
        power(a+1)
for test in range(10):
    t = int(input())
    n, p = map(int, input().split())
    res = 1
    power(0)
    print("#{} {}".format(t, res))