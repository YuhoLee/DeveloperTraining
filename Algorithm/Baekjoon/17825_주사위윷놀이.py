# 10, 20, 30 -> 지름길 spot
dir = [[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],
       [10,13,16,19,25,30,35,40],
       [20,22,24,25,30,35,40],
       [30,28,27,26,25,30,35,40]]

duplicate = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,1,0,0,1,0,0],
             [0,1,1,0,1,0,0],
             [0,1,0,1,0,1,0,0]]


def DFS(pp,c, location, score):
    global result
    # 횟수 10번 되었을 때 점수 비교
    if c >= 10:
        if result < score:
            result = score
        return

    for i in range(4):
        buff = location[:]
        idx,road = buff[i]

        # 끝까지 갔다면 이동할 필요가 없음 -> 다음 말을 이동하자!
        if idx == -1: continue

        if road == 0 and idx == 5: road,idx = 1,0
        elif road == 0 and idx == 10: road,idx = 2,0
        elif road == 0 and idx == 15: road,idx = 3,0

        if idx+arr[c] >= len(dir[road]):
            idx = -1
        else:
            idx = idx + arr[c]
            flag = False
            for j in range(4):
                if j != i and dir[road][idx] == dir[buff[j][1]][buff[j][0]] and duplicate[road][idx] == duplicate[buff[j][1]][buff[j][0]]:
                    if idx == -1 or buff[j][0] != -1:
                        flag = True
                        break
            if flag: continue
        buff[i] = (idx,road)
        pp.append(i)
        if idx != -1:
            DFS(pp[:],c+1, buff, score+dir[road][idx])
        else:
            DFS(pp[:],c+1, buff, score)
        pp.pop(-1)


arr = list(map(int, input().split()))
result = 0
DFS([],0, [(0,0),(0,0),(0,0),(0,0)],0)
print(result)
