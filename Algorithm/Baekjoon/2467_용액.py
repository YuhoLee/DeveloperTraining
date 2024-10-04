n = int(input())
arr = list(map(int, input().split()))

resAbs = 2 * pow(10,9)
res = (None, None)

for i in range(0, n-1):
    target = arr[i]
    ins,ine = i+1, n-1

    while ins <= ine:
        mid = (ins + ine) // 2
        tmp = target + arr[mid]

        if abs(tmp) < resAbs:
            resAbs = abs(tmp)
            res = (arr[i], arr[mid])

            if tmp == 0: break

        if tmp < 0:
            ins = mid + 1
        else:
            ine = mid - 1

print(res[0], res[1])