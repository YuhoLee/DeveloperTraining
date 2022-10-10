from collections import deque


# 원판의 합 계산
def calc_sum():
    return sum([sum(p) for p in plate])


# 해당 칸과 인접한 칸 찾아서 지워주기
def search(x,y):
    global cnt
    q = deque()
    q.append((x,y))
    visited[y][x] = True
    # 대상 숫자
    target = plate[y][x]
    c = 1
    while q:
        # 꺼내서 일단 지워주고 전체 개수를 1 줄임
        qx,qy = q.popleft()
        plate[qy][qx] = 0
        cnt -= 1
        # 사방 탐색
        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            px,py = qx+dx,qy+dy
            # 판과 판은 첫 인덱스와 끝 인덱스가 인접하지 않으므로 continue처리
            if not(0 <= py < n): continue
            # 판 내에 있는 숫자들은 원형이기에 처음 인덱스와 끝 인덱스가 인접할 수도 있음
            if px == m: px = 0
            # 방문하지 않고 인접한 숫자가 있으면
            if not visited[py][px] and plate[py][px] == target:
                # 삭제 개수 증가
                c += 1
                q.append((px,py))
                visited[py][px] = True
    # 삭제 개수가 1개보다 많으면 -> 인접한게 있음
    # 삭제 개수가 1개이면 -> 인접한거 없음
    if c > 1: return True
    else: return False


n,m,t = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(n)]
action = [list(map(int, input().split())) for _ in range(t)]
cnt = n*m

for x,d,k in action:
    visited = [[False]*m for _ in range(n)]
    for i in range(x,n+1):
        # x의 배수 원판에 대해
        if i % x == 0:
            # k번 반복
            for _ in range(k):
                # 시계 방향
                if d == 0:
                    plate[i-1].insert(0,plate[i-1].pop(-1))
                # 반시계 방향
                elif d == 1:
                    plate[i-1].append(plate[i-1].pop(0))

    # 인접 숫자 삭제 여부
    flag = False
    for i in range(n):
        for j in range(m):
            # 방문하지 않았으면 삭제한 숫자가 아닐 시
            if plate[i][j] != 0 and not visited[i][j]:
                # 해당 숫자를 임시로 저장해놓음
                buff = plate[i][j]
                # 인접한 숫자가 없었다면
                if not search(j,i):
                    # 방문 하지 않았던 걸로 하고, 원판에 기존 숫자를 넣으며 살아 있는 숫자 개수를 1 증가시켜줌
                    visited[i][j] = False
                    plate[i][j] = buff
                    cnt += 1
                # 인접 숫자 삭제 시행 O
                else: flag = True

    # 인접 숫자를 삭제 후 모두 0이 되었다면 탈출
    if cnt == 0: break

    # 인접숫자를 삭제하지 않았으며 삭제되지 않은 숫자 개수가 0이 아닐 시
    # 2번째 작업 수행
    if not flag and cnt > 0:
        avg = calc_sum() / cnt
        for i in range(n):
            for j in range(m):
                if 0 < plate[i][j] < avg: plate[i][j] += 1
                elif plate[i][j] > avg: plate[i][j] -= 1

print(calc_sum())
