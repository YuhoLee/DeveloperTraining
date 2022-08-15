import sys

n = int(sys.stdin.readline())
mtList = list(map(int, sys.stdin.readline().split(' ')))
mtList.sort()
s = 0
for i in range(n,0,-1):
    s += i * mtList[n-i]
print(s)