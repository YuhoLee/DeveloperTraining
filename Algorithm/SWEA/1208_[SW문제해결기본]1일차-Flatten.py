for t in range(10):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[arr.index(max(arr))] -= 1
        arr[arr.index(min(arr))] += 1
    print("#{} {}".format(t+1, max(arr) - min(arr)))
