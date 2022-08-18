def postorder(idx):
    if tree[idx][2] is None and tree[idx][3] is None:
        if tree[idx][0] in ['+','-','*','/']:
            return False
        else: return True
    n1 = postorder(tree[idx][2])
    n2 = postorder(tree[idx][3])
    oper = tree[idx][0]
    if n1 and n2 and oper in ['+','-','*','/']:
        return True
    else: return False


for t in range(1,11):
    n = int(input())
    # 0: item, 1: parent, 2: left, 3: right
    tree = [[None]*4 for _ in range(n+1)]
    for i in range(1,n+1):
        line = input().split()
        if line[1] not in ['+','-','*','/']:
            line[1] = int(line[1])
        tree[i][0] = line[1]
        if len(line) == 4:
            tree[i][2] = int(line[2])
            tree[i][3] = int(line[3])
            tree[int(line[2])][1] = i
            tree[int(line[3])][1] = i
    print("#{} {}".format(t,int(postorder(1))))
