SIZE = 300
t = int(input())
for test in range(1,t+1):
    n,m,k = map(int, input().split())
    arr = [[0]*(2*SIZE+m) for _ in range(SIZE)]
    arr += [[0]*SIZE + list(map(int, input().split())) + [0]*SIZE for _ in range(n)]
    arr += [[0]*(2*SIZE+m) for _ in range(SIZE)]

    # 세포가 저장될 리스트
    cell = []

    # 첫 시작은 SIZE,SIZE
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                print("({},{})".format(i,j))