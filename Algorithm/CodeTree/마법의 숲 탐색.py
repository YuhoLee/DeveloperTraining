from collections import deque

# 이동 조건
downMap = [[1, -1], [2, 0], [1, 1]]
erasedDownMap = [[0, -1], [-1, 0], [0, 1]]
filledDownMap = [[1, -1], [2, 0], [1, 1]]
leftDownMap = [[-1, -1], [0, -2], [1, -1], [1, -2], [2, -1]]
erasedLeftDownMap = [[0, 0], [-1, 0], [0, 1]]
filledLeftDownMap = [[1, -1], [1, -2], [2, -1]]
rightDownMap = [[-1, 1], [0, 2], [1, 1], [1, 2], [2, 1]]
erasedRightDownMap = [[0, 0], [-1, 0], [0, -1]]
filledRightDownMap = [[1, 1], [1, 2], [2, 1]]
# 방향
dirMap = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# 기본 십자모양
shapeMap = [0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]


class Fairy:
    def __init__(self, idx, x, y, dir):
        self.idx = idx
        self.dir = dir
        self.x = x
        self.y = y

    def start(self):
        for dy, dx in shapeMap:
            forest[self.y + dy][self.x + dx] = self.idx

    def downMovable(self):
        global forest, r, c
        if not (0 <= self.y + 2 < r): return False

        for dy, dx in downMap:
            if forest[self.y + dy][self.x + dx] is not None:
                return False
        else:
            return True

    def leftDownMovable(self):
        global forest, r, c
        if not (0 <= self.y + 2 < r) or not (0 <= self.x - 2 < c): return False

        for dy, dx in leftDownMap:
            if forest[self.y + dy][self.x + dx] is not None:
                return False
        else:
            return True

    def rightDownMovable(self):
        global forest, r, c
        if not (0 <= self.y + 2 < r) or not (0 <= self.x + 2 < c): return False

        for dy, dx in rightDownMap:
            if forest[self.y + dy][self.x + dx] is not None:
                return False
        else:
            return True

    def isOver(self):
        return self.y - 1 <= 2

    def moveDown(self):
        global forest, r, c

        for dy, dx in erasedDownMap:
            forest[self.y + dy][self.x + dx] = None
        for dy, dx in filledDownMap:
            forest[self.y + dy][self.x + dx] = self.idx
        self.y += 1

    def moveLeftDown(self):
        global forest, r, c

        for dy, dx in erasedLeftDownMap:
            forest[self.y + dy][self.x + dx] = None
        for dy, dx in filledLeftDownMap:
            forest[self.y + dy][self.x + dx] = self.idx
        self.y += 1
        self.x -= 1
        self.dir = (self.dir - 1) % 4

    def moveRightDown(self):
        global forest, r, c

        for dy, dx in erasedRightDownMap:
            forest[self.y + dy][self.x + dx] = None
        for dy, dx in filledRightDownMap:
            forest[self.y + dy][self.x + dx] = self.idx
        self.y += 1
        self.x += 1
        self.dir = (self.dir + 1) % 4


res = []
r, c, k = tuple(map(int, input().split()))
r += 3
forest = [[None] * c for _ in range(r)]
fairyList = []

for i in range(k):
    x, dir = tuple(map(int, input().split()))
    fairyList.append(Fairy(idx=i, x=x - 1, y=1, dir=dir))


def move(fairy: Fairy):
    global forest, r, c

    fairy.start()
    while True:
        if fairy.downMovable():
            fairy.moveDown()
        else:
            if fairy.leftDownMovable():
                fairy.moveLeftDown()
            else:
                if fairy.rightDownMovable():
                    fairy.moveRightDown()
                else:
                    if fairy.isOver():
                        forest = [[None] * c for _ in range(r)]
                        break

                    bfs(fairy)
                    break


def bfs(fairy: Fairy):
    global fairyList, res, forest, r, c

    buff = []
    visited = [[False] * c for _ in range(r)]
    q = deque()
    q.append((fairy.idx, fairy.y, fairy.x))
    for dy, dx in shapeMap:
        py, px = fairy.y + dy, fairy.x + dx
        visited[py][px] = True

    while q:
        idx, y, x = q.popleft()
        buff.append(y+1)

        # 출입구
        tf = fairyList[idx]
        tdy,tdx = dirMap[tf.dir]
        ty,tx = y+tdy, x+tdx
        if tf.dir == 0:
            searchPoints = [[0,-1], [-1,0], [0,1]]
        elif tf.dir == 1:
            searchPoints = [[-1,0], [0,1], [1,0]]
        elif tf.dir == 2:
            searchPoints = [[0,-1], [1,0], [0,1]]
        else: # 3
            searchPoints = [[0,-1], [-1,0], [1,0]]

        for tddy,tddx in searchPoints:
            ry,rx = ty+tddy, tx+tddx
            if not (0 <= ry < r and 0 <= rx < c): continue
            if forest[ry][rx] is not None and not visited[ry][rx]:
                targetFairy = fairyList[forest[ry][rx]]
                q.append((targetFairy.idx, targetFairy.y, targetFairy.x))
                for dy, dx in shapeMap:
                    py, px = targetFairy.y + dy, targetFairy.x + dx
                    visited[py][px] = True

    res.append(max(buff) - 2)


for fairy in fairyList:
    move(fairy)
print(sum(res))
