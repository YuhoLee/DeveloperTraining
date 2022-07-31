# BFS
class Queue:
    def __init__(self):
        self.items = []
        self.size = 0
    def append(self, item):
        self.items.append(item)
        self.size += 1
    def pop(self):
        self.size -= 1
        return self.items.pop(0)
    def getSize(self):
        return self.size

def action(idx, p):
    count = 0
    # 벽에 가로막혀있지 않고 구멍에 도달할 때까지 해당 방향으로 직진
    while arr[idx[0]+dir[p][0]][idx[1]+dir[p][1]] != '#' and (arr[idx[0]][idx[1]] != 'O'):
        idx[0] += dir[p][0]
        idx[1] += dir[p][1]
        count += 1
    # 움직인 결과 위치와 움직인 횟수 반환
    return idx, count

h, w = tuple(map(int, input().split(' ')))
arr = [list(input()) for _ in range(h)]

for i,ar in enumerate(arr):
    # 빨간 구슬 위치
    if 'R' in ar:
        r = [i,ar.index('R')]
        arr[r[0]][r[1]] = '.'
    # 파란 구슬 위치
    if 'B' in ar:
        b = [i,ar.index('B')]
        arr[b[0]][b[1]] = '.'
    # 구멍 위치
    if 'O' in ar:
        o = [i,ar.index('O')]

result = 0
q = Queue()
# 위, 아래, 왼쪽, 오른쪽
dir = [[-1,0], [1,0], [0,-1], [0,1]]

# 처음 위치 및 카운트 Queue에 Push
init_set = (r, b, 1)
q.append(init_set)

# 목표지점에 도달하면 result가 바뀌는데, 이 때 반복문 종료
while result == 0:
    r_pin, b_pin, cnt = q.pop()
    if cnt > 10:
        result = -1
        break

    # 상하좌우 네 방향에 대해서
    for i in range(4):
        # 이런 조건이 굉장히 중요: 중복을 피할 수 있음
        # 벽에 막혀있지 않은 방향일 시
        if arr[r_pin[0]+dir[i][0]][r_pin[1]+dir[i][1]] != "#" or arr[b_pin[0] + dir[i][0]][b_pin[1] + dir[i][1]] != "#":
            # 벽에 막힐 때까지 빨간 구슬, 파란 구슬 이동!
            r_idx, r_dis = action(r_pin[:], i)
            b_idx, b_dis = action(b_pin[:], i)

            # 파란 구슬이 구멍에 빠진다면 빨간 구슬이 빠진다 해도 실패이므로 파란 구슬 먼저 검사
            # 파란 구슬이 구멍에 빠진다면 실패... -> 다음 케이스로 넘어감
            # 빨간 구슬이 구멍에 빠진다면 성공!!! -> 움직인 횟수 반환하고 종료
            if b_idx[0] == o[0] and b_idx[1] == o[1]:
                continue
            if r_idx[0] == o[0] and r_idx[1] == o[1]:
                result = cnt
                break

            # 빨간 구슬과 파란 구슬이 같은 지점에 위치할 수 없기에
            # 더 많이 움직인 구슬이 움직인 방향과 반대 방향으로 한 칸 이동
            if r_idx[0] == b_idx[0] and r_idx[1] == b_idx[1]:
                if r_dis < b_dis:
                    b_idx[0] -= dir[i][0]
                    b_idx[1] -= dir[i][1]
                else:
                    r_idx[0] -= dir[i][0]
                    r_idx[1] -= dir[i][1]

            # 움직인 후의 빨간 구슬과 파란 구슬, 그리고 움직인 횟수를 Queue에 push
            q.append((r_idx, b_idx, cnt + 1))
print(result)