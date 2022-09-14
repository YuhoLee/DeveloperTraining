def DFS(p):
    if tree[p][1] is None and tree[p][2] is None:
        return 1
    ch1,ch2 = 0,0
    if tree[p][1] is not None:
        ch1 = DFS(tree[p][1])
    if tree[p][2] is not None:
        ch2 = DFS(tree[p][2])
    return ch1+ch2+1


t = int(input())
for test in range(1,t+1):
    v,e,n1,n2 = map(int, input().split())
    arr = list(map(int, input().split()))
    mm = max(arr)
    tree = [[None,None,None] for _ in range(mm+1)]
    for i in range(0,len(arr),2):
        parent,child = arr[i], arr[i+1]
        if tree[parent][1] is None: tree[parent][1] = child
        else: tree[parent][2] = child
        tree[child][0] = parent

    l1,l2 = [],[]
    parent = tree[n1][0]
    while parent is not None:
        l1.append(parent)
        parent = tree[parent][0]
    parent = tree[n2][0]
    while parent is not None:
        l2.append(parent)
        parent = tree[parent][0]
    res = float('inf')
    len1 = len(l1)
    len2 = len(l2)
    idx = -1
    while True:
        if len1 < -idx or len2 < -idx: break
        else:
            if l1[idx] != l2[idx]:
                break
        res = l1[idx]
        idx -= 1
    cc = DFS(res)
    print("#{} {} {}".format(test,res,cc))