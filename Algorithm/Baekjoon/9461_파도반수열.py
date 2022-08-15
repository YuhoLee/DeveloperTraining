import sys

p = [0]*101
p[1],p[2],p[3],p[4],p[5] = 1,1,1,2,2
testcase = int(sys.stdin.readline())
for _ in range(testcase):
    n = int(sys.stdin.readline())
    for i in range(6,n+1):
        p[i] = p[i-1] + p[i-5]
    print(p[n])