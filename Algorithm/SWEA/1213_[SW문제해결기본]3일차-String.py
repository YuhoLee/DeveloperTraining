for t in range(10):
    test = int(input())
    s = input()
    l = len(s)
    sen = input()
    c = 0
    idx = sen.find(s)
    while idx != -1:
        c += 1
        sen = sen[idx+l:]
        idx = sen.find(s)
    print("#{} {}".format(test,c))