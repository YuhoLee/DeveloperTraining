n,k = map(int, input().split())
arr = list(map(int, input().split()))
diff = []
for i in range(len(arr)-1):
    diff.append(arr[i+1]-arr[i])
diff.sort(reverse=True)
print(sum(diff[k-1:]))