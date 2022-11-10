n = int(input())
arr = list(map(int, input().split()))

aa,ab,ac = arr
ia,ib,ic = arr

for i in range(1,n):
    f,s,t = map(int, input().split())
    arr[0],arr[1],arr[2] = f,s,t
    raa = max(aa, ab) + arr[0]
    rab = max(aa, ab, ac) + arr[1]
    rac = max(ab, ac) + arr[2]
    ria = min(ia, ib) + arr[0]
    rib = min(ia, ib, ic) + arr[1]
    ric = min(ib, ic) + arr[2]

    aa,ab,ac = raa,rab,rac
    ia,ib,ic = ria,rib,ric

print("{} {}".format(max(aa,ab,ac), min(ia,ib,ic)))