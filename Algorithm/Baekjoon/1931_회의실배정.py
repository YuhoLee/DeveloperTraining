import sys

n = int(sys.stdin.readline())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, sys.stdin.readline().split(' '))))
meeting = sorted(meeting,key=lambda x: (x[1], x[0]))

cnt = 1
curr = meeting[0]
i = 1
while(i < n):
    if curr[1] <= meeting[i][0]:
        cnt += 1
        curr = meeting[i]
    i += 1
print(cnt)