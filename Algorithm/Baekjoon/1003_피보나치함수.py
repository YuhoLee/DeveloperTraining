import sys

def fib(x):
    if x==0 or x==1:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fib(x-1) + fib(x-2)
    return d[x]

testcase = int(sys.stdin.readline())
for _ in range(testcase):
    n = int(sys.stdin.readline())
    d = [0] * 41
    if n==0:
        print("1 0")
    elif n==1:
        print("0 1")
    else:
        print(fib(n-2), fib(n-1))