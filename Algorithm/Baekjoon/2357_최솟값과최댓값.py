import heapq

n, m = tuple(map(int, input().split()))
minTree = [0] * n * 4
maxTree = [pow(10, 9) + 1] * n * 4
node = [0]
for _ in range(n):
    node.append(int(input()))


def createMinTree(start: int, end: int, idx: int):
    if start == end:
        minTree[idx] = node[start]
        return node[start]

    mid = (start + end) // 2
    minTree[idx] = min(createMinTree(start, mid, idx * 2), createMinTree(mid + 1, end, idx * 2 + 1))
    return minTree[idx]


def createMaxTree(start: int, end: int, idx: int):
    if start == end:
        maxTree[idx] = node[start]
        return node[start]

    mid = (start + end) // 2
    maxTree[idx] = max(createMaxTree(start, mid, idx * 2), createMaxTree(mid + 1, end, idx * 2 + 1))
    return maxTree[idx]


createMinTree(1, n, 1)
createMaxTree(1, n, 1)


def calcMinTree(start: int, end: int, left: int, right: int, idx: int):
    if right < start or left > end: return pow(10, 9)
    if left <= start and end <= right: return minTree[idx]

    mid = (start + end) // 2
    return min(calcMinTree(start, mid, left, right, idx * 2), calcMinTree(mid + 1, end, left, right, idx * 2 + 1))


def calcMaxTree(start: int, end: int, left: int, right: int, idx: int):
    if right < start or left > end: return 0
    if left <= start and end <= right: return maxTree[idx]

    mid = (start + end) // 2
    return max(calcMaxTree(start, mid, left, right, idx * 2), calcMaxTree(mid + 1, end, left, right, idx * 2 + 1))


for _ in range(m):
    a, b = tuple(map(int, input().split()))
    print(calcMinTree(1, n, a, b, 1), calcMaxTree(1, n, a, b, 1))