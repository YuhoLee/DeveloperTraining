test = 0
while(True):
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        count = 0
        for i in range(2, len(arr)-2):
            if arr[i-2] < arr[i] and arr[i-1] < arr[i] and arr[i+1] < arr[i] and arr[i+2] < arr[i]:
                count += (arr[i] - max(arr[i-2],arr[i-1],arr[i+1],arr[i+2]))
        test += 1
        print("#{} {}".format(test, count))
    except:
        break