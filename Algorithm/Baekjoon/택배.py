# init
n,c = map(int, input().split())
m = int(input())
task = [list(map(int, input().split())) for _ in range(m)]
# 도착 지점을 기준으로 정렬
task.sort(key=lambda a: a[1])

# 해당 지점에서 수용 가능한 택배량
capacity = [c] * (n+1)

# 최종 배달된 양
res = 0

for s,e,cap in task:
    # 초기 수용 가능한 양을 최대 수용 가능량으로 설정
    can = c
    # start에서 end로 갈 때까지

    for i in range(s,e):
        # s~e까지에서 현재 수용할 수 있는 택배량 중 가장 작은 것을 찾음
        can = min(can,capacity[i])
    # 찾은 택배량이 현재 지점의 박스 개수보다 작은지 큰지 확인
    can = min(can,cap)

    # s~e에서 can 만큼 가지고 있기 때문에
    # 수용할 수 있는 양인 capacity를 s~e 범위에서 can만큼 줄여줌
    for i in range(s,e):
        capacity[i] -= can
    # can은 운송될 양이기 때문에 res에 더해줌
    res += can
print(res)


