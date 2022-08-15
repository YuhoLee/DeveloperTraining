import sys

score = [0]
max_score = [[0,0]]
n = int(sys.stdin.readline())
for _ in range(n):
    score.append(int(sys.stdin.readline()))

if n==1:
    print(score[1])
else:
    max_score.append([0,score[1]])
    max_score.append([score[2],score[1]+score[2]])
    for i in range(3,n+1):
        v1 = max(max_score[i-2][0], max_score[i-2][1]) + score[i]
        v2 = max_score[i-1][0] + score[i]
        max_score.append([v1,v2])

    print(max(max_score[n]))