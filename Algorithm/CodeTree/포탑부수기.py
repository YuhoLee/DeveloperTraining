# N*M격자, 포탑 개수는 N*M개
# 포탑에는 공격력이 있음, 공격력이 늘거나 줄 수 있으며, 공격력이 0이 되면 포탑 파괴

# [1] 공격자 선정
# 공격자로 선정되면 핸디캡 적용(N+M만큼 공격력 증가)
# 약한 포탑의 기준
# (1) 공격력이 가장낮음.
# (2) 가장 낮은 포탑이 두개 이상이라면 가장 최근에 공격한 포탑이 가장 약한 포탑임.
# (3) 만약 그런 포탑도 여러개라면 행과 열의 합이 가장 큰 포탑이 가장 약한 포탑.
# (4) 이러한 포탑도 여러개라면 열값이 가장 큰 포탑이 가장 약한 포탑.

# [2] 공격자 공격
# 자신을 제외한 가장 강한 포탑을 공격
# 강한 포탑 기준
# (1) 공격력이 가장 높음.
# (2) 여러개라면 공격한지 가장 오래된 포탑이 가장 강한 포탑.
# (3) 그런 포탑도 여러개라면 행과 열의 합이 가장 작은 포탑이 가장 강한 포탑.
# (4) 이러한 포탑도 여러개라면 열값이 가장 작은 포탑이 가장 강한 포탑.

# 강한 포탑의 공격 방식은 레이저와 포탄이 있으며, 먼저 레이저를 시도하고 안되면 포탑을 시도.
# (1) 레이저 공격
# 레이저 공격은 부서진 포탑 위치를 지날 수 없음. 살아있는 포탑은 지날수있음
# 살아있는 포탑을 지날때, 절반의 데미지를 입힘.
# 경계를 넘는 것은 가능(인덱스 넘칠 시 0으로 가서 공격)
# 우/하/좌/상 순서로 경로 선택, 사방탐색할때 인덱스 넘치는 경우도 확인해봐야함.
# (2) 포탄 공격
# 포탄을 던짐. 공격자의 공격력만큼 피해를 받음.
# 주위의 8개 방향에 있는 포탑도 피해를 입으며 경계를 넘는 것이 가능.
# 절반만큼 피해를 받으며, 절반은 몫을 말함.

# [3] 공격력이 0 이하가 되면 포탑이 부셔짐.
# [4] 공격과 무관했던 포탑은 공격력이 1씩 올라감. 공격을 하지도, 받지도 않은 포탑.

# 모든 턴이 지난 이후 남아있는 가장 강한 포탑의 공격력을 출력하도록 해라.

from collections import deque

class Turret:
    def __init__(self, f):
        # 공격력
        self.f = f
        # 마지막 공격 턴
        self.lastFt = -1
        # 공격 참여 여부
        self.isJoin = False

    def __str__(self):
        return "{0}".format(self.f)


N,M,K = tuple(map(int, input().split()))
handicap = N*M
inputList = [list(map(int, input().split())) for _ in range(N)]
mMap = [[None] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        tf = int(inputList[i][j])
        mMap[i][j] = Turret(tf)


def selectAttacker():
    global mMap

    force = float('inf')
    ay = ax = -1
    lastFt = -1
    for i in range(N):
        for j in range(M):
            # 빈칸이거나 파괴된 포탑은 제외
            if mMap[i][j] is None or mMap[i][j].f <= 0: continue
            tg = mMap[i][j]
            # 공격력 비교
            if tg.f < force:
                force,ay,ax,lastFt = tg.f,i,j,tg.lastFt
                # 공격력 같은 경우
            elif tg.f == force:
                if tg.lastFt > lastFt:
                    force,ay,ax,lastFt = tg.f,i,j,tg.lastFt
                elif tg.lastFt == lastFt:
                    if i+j > ay+ax:
                        force, ay, ax, lastFt = tg.f, i, j, tg.lastFt
                    elif i+j == ay+ax:
                        if j > ax:
                            force, ay, ax, lastFt = tg.f, i, j, tg.lastFt

    return ay,ax


def selectTarget():
    global mMap

    force = -1
    ty, tx = N,M
    lastFt = 1001
    for i in range(N):
        for j in range(M):
            # 빈칸이거나 파괴된 포탑은 제외
            if mMap[i][j] is None or mMap[i][j].f <= 0: continue

            tg = mMap[i][j]
            # 공격력 비교
            if tg.f > force:
                force, ty, tx, lastFt = tg.f, i, j, tg.lastFt
                # 공격력 같은 경우
            elif tg.f == force:
                if tg.lastFt < lastFt:
                    force, ty, tx, lastFt = tg.f, i, j, tg.lastFt
                elif tg.lastFt == lastFt:
                    if i + j < ty + tx:
                        force, ty, tx, lastFt = tg.f, i, j, tg.lastFt
                    elif i + j == ty + tx:
                        if j < tx:
                            force, ty, tx, lastFt = tg.f, i, j, tg.lastFt

    return ty, tx


dir = [[0,1],[1,0],[0,-1],[-1,0]]
visited = [[False] * M for _ in range(N)]


def BFS():
    global mMap, visited, say, sax, sty, stx, dir

    q = deque()
    q.append([say,sax,0,[]])

    while q:
        cy,cx,length,path = q.popleft()
        for dy,dx in dir:
            py,px = cy+dy, cx+dx
            # 빈칸이 아니거나
            if py < 0: py = N-1
            if py >= N: py = 0
            if px < 0: px = M-1
            if px >= M: px = 0
            # 방문한 경우 -> 스킵
            if visited[py][px]: continue
            # 죽은 포탑인 경우 -> 스킵
            if mMap[py][px] is not None and mMap[py][px].f <= 0: continue

            visited[py][px] = True

            # 공격 대상이라면
            if py == sty and px == stx:
                return length+1, path[:]
            else:
                # 빈칸이라면 그냥 진행
                if mMap[py][px] is None:
                    q.append([py,px,length+1,path[:]])
                # 포탑이면서 살아있는 포탑인 경우
                elif isinstance(mMap[py][px], Turret) and mMap[py][px].f > 0:
                    copyPath = path[:]
                    copyPath.append([py,px])
                    q.append([py,px,length+1,copyPath])

    return float('inf'),[]


def RaiserAttack():
    global mMap, N, M
    visited[say][sax] = True
    length, damagedTurrets = BFS()

    if length != float('inf'):
        damage = mMap[say][sax].f
        halfDamage = damage // 2

        mMap[sty][stx].f -= damage
        mMap[sty][stx].isJoin = True
        for dty,dtx in damagedTurrets:
            mMap[dty][dtx].f -= halfDamage
            mMap[dty][dtx].isJoin = True

        return True
    else:
        return False


def BombAttack():
    damage = mMap[say][sax].f
    halfDamage = damage // 2
    mMap[sty][stx].f -= damage

    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            if dy == 0 and dx == 0: continue
            py,px = sty + dy, stx + dx
            if py < 0: py = N - 1
            if py >= N: py = 0
            if px < 0: px = M - 1
            if px >= M: px = 0
            if py == say and px == sax: continue
            mMap[py][px].f -= halfDamage
            mMap[py][px].isJoin = True


def attack():
    global visited
    isRaiser = RaiserAttack()
    visited = [[False] * M for _ in range(N)]
    if not isRaiser:
        BombAttack()


def fixTurret():
    turretCnt = 0
    for i in range(N):
        for j in range(M):
            if mMap[i][j].isJoin:
                mMap[i][j].isJoin = False
            else:
                # 수리
                if mMap[i][j].f > 0:
                    mMap[i][j].f += 1

            # 터렛 카운트
            if mMap[i][j].f > 0:
                turretCnt += 1

    return turretCnt


for kk in range(K):
    say,sax = selectAttacker()
    sty, stx = selectTarget()

    mMap[say][sax].f += (N+M)
    mMap[say][sax].lastFt = kk
    mMap[say][sax].isJoin = True
    mMap[sty][stx].isJoin = True

    attack()
    remainTurretCnt = fixTurret()

    if remainTurretCnt <= 1:
        break



maxF = -1
for i in range(N):
    for j in range(M):
        if mMap[i][j].f > 0:
            force = mMap[i][j].f
            maxF = max(maxF, force)
print(maxF)
