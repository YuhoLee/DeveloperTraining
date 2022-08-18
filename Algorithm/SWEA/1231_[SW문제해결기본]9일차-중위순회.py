def inorder(s):
    if s <= n:
        inorder(s*2)
        print(alpha[s],end='')
        inorder(s*2+1)


for t in range(1,11):
    n = int(input())
    alpha = [0]*(n+1)
    for i in range(1,n+1):
        line = input().split()
        alpha[i] = line[1]
    print("#{} ".format(t),end='')
    inorder(1)
    print()