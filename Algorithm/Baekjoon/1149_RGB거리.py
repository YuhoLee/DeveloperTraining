import sys

RGBlist = []
n = int(sys.stdin.readline())
for i in range(n):
    l = list(map(int, sys.stdin.readline().split(' ')))
    RGBlist.append(l)
for i in range(1,n):
    RGBlist[i][0] = RGBlist[i][0] + min(RGBlist[i-1][1],RGBlist[i-1][2])
    RGBlist[i][1] = RGBlist[i][1] + min(RGBlist[i-1][2],RGBlist[i-1][0])
    RGBlist[i][2] = RGBlist[i][2] + min(RGBlist[i-1][0],RGBlist[i-1][1])

print(min(RGBlist[n-1]))