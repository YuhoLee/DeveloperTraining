num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

t = int(input())
for test in range(1,t+1):
    n = int(input()[3:])
    print(n)
    string = list(input().split())
    count = [0] * 10
    for s in string:
        for i in range(10):
            if s == num[i]:
                count[i] += 1
    res = [0] * n
    idx = 0
    for i in range(10):
        for j in range(count[i]):
            res[idx] = num[i]
            idx += 1
    print("#{}".format(test))
    print(' '.join(res))