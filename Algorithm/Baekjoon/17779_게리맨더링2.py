def calc(x, y, d1, d2):
    population = [0,0,0,0,0]
    area = [[0]*n for _ in range(n)]

    # area5 영역을 채워줌
    for i in range(d1+1):
        area[x+i][y-i] = 5
        area[x+d2+i][y+d2-i] = 5
    for j in range(d2+1):
        area[x+j][y+j] = 5
        area[x+d1+j][y-d1+j] = 5

    # area1 영역에 대한 인구수 계산
    for i in range(x+d1):
        c = 0
        while area[i][c] == 0 and c <= y:
            population[0] += arr[i][c]
            c += 1

    # area2 영역에 대한 인구수 계산
    for i in range(x + d2+1):
        c = n-1
        while area[i][c] == 0 and c > y:
            population[1] += arr[i][c]
            c -= 1

    # area3 영역에 대한 인구수 계산
    for i in range(x+d1, n):
        c = 0
        while area[i][c] == 0 and c < y-d1+d2:
            population[2] += arr[i][c]
            c += 1

    # area4 영역에 대한 인구수 계산
    for i in range(x + d2 +1, n):
        c = n-1
        while area[i][c] == 0 and c >= y-d1+d2:
            population[3] += arr[i][c]
            c -= 1

    # 전체에서 각 영역 인구의 합을 빼주면 area5의 인구가 나옴
    population[4] = total-sum(population)
    return max(population)-min(population)


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = float('inf')
total = 0
for i in range(n):
    total += sum(arr[i])

for x in range(0, n):
    for y in range(0, n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if x+d1+d2 < n and y-d1>=0 and y+d2<n:
                    res = min(res, calc(x, y, d1, d2))
print(res)