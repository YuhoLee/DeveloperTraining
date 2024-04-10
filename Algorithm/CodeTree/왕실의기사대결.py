# 기사 이동
# 명령 받은 기사는 상하좌우로 이동 가능
# 이동하려는 위치에 다른 기사가 있다면 그 기사도 밀려나게 됨.
# 밀리는 기사가 이동할 위치가 벽인 경우에는 아무것도 움직이지 않음.
# 체스판에서 사라지는 기사에게 명령을 내리면 아무것도 움직이지 않음.

# 기사 대결
# 기사가 밀쳐난 자리에 함정이 있으면 피해를 입음.

# 결과는 왕의 명령이 모두 수행된 이후 생존한 기사들이 입은 피해의 합을 출력

# L은 체스판의 크기
# N은 초기 기사들의 정보 입력 횟수
# Q는 왕의 명령 횟수

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]


class Knight:
    def __init__(self, idx, r, c, h, w, k):
        self.idx = idx
        self.position = []
        self.buff_position = []
        self.life = k
        # 누적 데미지
        self.total_damage = 0
        # 임시 데미지
        self.buff_damage = 0
        for i in range(r, r + h):
            for j in range(c, c + w):
                self.position.append([i, j])
                self.buff_position.append([i, j])

    def getPositions(self):
        ss = ""
        for y,x in self.position:
            ss += "({0},{1})/".format(y,x)
        return ss

    def isLive(self):
        return self.life - self.total_damage > 0


# 왕의 명령 수행
def command(pos, d):
    global field, k_field, knight_list, searched, N

    knight = knight_list[pos]
    if not knight.isLive(): return
    isSuccess = researchNextKnight(knight, d)

    if isSuccess:
        k_field = [[-1] * (L + 2) for _ in range(L + 2)]

        for res_knight in knight_list:
            if res_knight.idx != pos:
                res_knight.total_damage += res_knight.buff_damage

            res_knight.position = res_knight.buff_position.copy()

            # 살아있는 기사만 다시 그려줌
            if res_knight.isLive():
                for ky,kx in res_knight.position:
                    k_field[ky][kx] = res_knight.idx

    for res_knight in knight_list:
        res_knight.buff_damage = 0
        res_knight.buff_position = res_knight.position.copy()

    searched = [False] * N

    print("after")
    for k in knight_list:
        print(k.getPositions())


def researchNextKnight(knight, d):
    global field, k_field, knight_list, searched

    dy, dx = dir[d]
    next_idx_list = []
    knight.buff_position.clear()
    for (y, x) in knight.position:
        py, px = y + dy, x + dx
        knight.buff_position.append([py,px])

        # 벽인 경우에는 그냥 false return
        if field[py][px] == "W": return False

        if k_field[py][px] != -1 and k_field[py][px] != knight.idx:
            if k_field[py][px] not in next_idx_list and not searched[k_field[py][px]]:
                searched[k_field[py][px]] = True
                next_idx_list.append(k_field[py][px])

    for target_idx in next_idx_list:
        next_knight = knight_list[target_idx]
        isMovable = researchNextKnight(next_knight, d)
        if not isMovable: return False

    for (y, x) in knight.buff_position:
        # 트랩이라면 데미지
        if field[y][x] == "T":
            knight.buff_damage += 1

    return True


L, N, Q = tuple(map(int, input().split()))

field = [[2] + list(map(int, input().split())) + [2] for _ in range(L)]
field.insert(0, [2] * (L + 2))
field.append([2] * (L + 2))

for i in range(L + 2):
    for j in range(L + 2):
        if field[i][j] == 1:
            # 트랩
            field[i][j] = "T"
        elif field[i][j] == 2:
            # 벽
            field[i][j] = "W"
        else:
            # 빈 공간
            field[i][j] = "E"

# 나이트 위치 정보
knight_list = []
searched = [False] * N
# 나이트 맵
k_field = [[-1] * (L + 2) for _ in range(L + 2)]
for k_idx in range(N):
    knight_buff = []
    r, c, h, w, k = tuple(map(int, input().split()))
    knight_list.append(Knight(k_idx, r, c, h, w, k))

    for i in range(r, r + h):
        for j in range(c, c + w):
            k_field[i][j] = k_idx

# 왕의 명령 리스트
command_list = []
for _ in range(Q):
    i, d = tuple(map(int, input().split()))
    command_list.append([i - 1, d])

for i, (pos, d) in enumerate(command_list):
    print("command")
    print(pos, d)
    print("before")
    for k in knight_list:
        print(k.getPositions())
    command(pos, d)

    for r in k_field:
        for c in r:
            if c == -1:
                print("e", end=" ")
            else: print(c, end=" ")
        print()

    print("\n")


res = 0
for knight in knight_list:
    if knight.isLive():
        res += knight.total_damage

print(res)