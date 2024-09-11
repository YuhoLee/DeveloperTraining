n, m, k = tuple(map(int, input().split()))
node = [None]
for _ in range(n):
    node.append(int(input()))

tree = [0] * (n * 4)


def create(start: int, end: int, idx: int):
    if start == end:
        tree[idx] = node[start]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = create(start, mid, idx * 2) + create(mid + 1, end, idx * 2 + 1)
    return tree[idx]


def calc(start: int, end: int, idx: int, left: int, right: int):
    if right < start or left > end: return 0
    if start >= left and end <= right: return tree[idx]

    mid = (start + end) // 2
    return calc(start, mid, idx * 2, left, right) + calc(mid + 1, end, idx * 2 + 1, left, right)


def update(start: int, end: int, idx: int, target: int, num: int):
    if start == end:
        diff = num - tree[idx]
        tree[idx] = num
        return diff

    mid = (start + end) // 2
    if start <= target <= mid:
        diff = update(start, mid, idx * 2, target, num)
        tree[idx] += diff
        return diff
    elif mid + 1 <= target <= end:
        diff = update(mid+1, end, idx * 2 + 1, target, num)
        tree[idx] += diff
        return diff


create(1,n,1)

for _ in range(m+k):
    a,b,c = tuple(map(int, input().split()))
    if a == 1:
        update(1, n, 1, b, c)
    elif a == 2:
        res = calc(1, n, 1, b, c)
        print(res)

