import sys

t = [0]*1000001
t[1] = 1
t[2] = 2
n = int(sys.stdin.readline())
for i in range(3,n+1):
    t[i] = (t[i-1] + t[i-2]) % 15746

print(t[n])